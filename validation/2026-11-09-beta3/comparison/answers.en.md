# The six complete comparison answers

The six research-answer bodies below are unchanged from the reviewed English edition. Primary-source URLs remain in the prose and each answer's structured source list. The structured fields are part of the authored answers; separate evaluator outputs, test fixtures and execution records are not included.

The [Latvian answers](answers.lv.md) and the [published findings](../../../PUBLISHED_FINDINGS.md) provide the corresponding original-language answers and reported comparison outcome. This translation is not a new research run. See the [publication scope](../../../PUBLICATION_SCOPE.md) for the evidence limits.

## baseline / IT01-depth-output

**There is no basis for adding the unit `m` to this checkpoint's output.** The card for `depth-anything/Depth-Anything-V2-Small-hf` identifies its output as relative depth, and the authors' repository also classifies the base models as relative-depth estimators. The card's general statement about relative and absolute depth does not establish that this particular checkpoint outputs metres. [Model card](https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf), [authors' repository](https://github.com/DepthAnything/Depth-Anything-V2).

The project author explains that the model predicts inverse depth: a smaller prediction corresponds to a more distant point. The component can therefore be retained for ordering image regions by relative proximity. That ordering does not itself provide physical distances in metres. [Author's explanation](https://github.com/DepthAnything/Depth-Anything-V2/issues/174).

The next step is to choose a separate checkpoint adapted for metric depth, such as `Depth-Anything-V2-Metric-Indoor-Small-hf` for indoor scenes. The author has already adapted that model, so you do not need to train a new one yourself. Under this task's action codes, however, the choice is `replace_core`. Before relying on its distances, measure its error on your own images against measured distances. [Metric model card](https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf). A user in the project discussion describes incorrect scale when constructing a point cloud; that is a report of a particular experience, not a universal error measurement. [Experience report](https://github.com/DepthAnything/Depth-Anything-V2/issues/152).

I checked sources and configuration here. I did not run inference, install packages or download weights.

## evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "relative_depth",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "depth_ordering"
  },
  "explanation": "Depth-Anything-V2-Small-hf is a relative-depth checkpoint. Its output represents the relative proximity of image points, and the task's stated conditions do not justify a scale in metres. The project author explains that it predicts inverse depth. Adding a metre label does not turn the output into a metric distance.",
  "next_step": "Retain this model for ordering nearer and more distant image regions. For distances in metres, choose a separate checkpoint that the authors have adapted for metric depth, such as Depth-Anything-V2-Metric-Indoor-Small-hf for indoor scenes. Before use, check its error on your own images against measured distances. Only sources were checked here.",
  "sources": [
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf",
    "https://github.com/DepthAnything/Depth-Anything-V2",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf/blob/main/config.json",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Metric-Indoor-Small-hf",
    "https://github.com/DepthAnything/Depth-Anything-V2/blob/main/metric_depth/README.md",
    "https://github.com/DepthAnything/Depth-Anything-V2/issues/174"
  ]
}
```

## baseline / IT02-clip-generation

**The official CLIP `ViT-B/32` does not generate a free-form descriptive sentence through the specified example.** `encode_image` and `encode_text` return feature vectors. Calling the model with an image and texts returns their similarities; the example supplies the texts in advance and scores those candidates. [Documented example and API](https://github.com/openai/CLIP).

This is also visible in `clip/model.py`: the text encoder produces a vector, while `forward` normalizes both types of vectors and returns similarity matrices. That execution path has no step that generates tokens for a new sentence. The requested free-form description would require a different or additional trained component with a text decoder, which is `replace_core` under the task's action codes. [Model code](https://github.com/openai/CLIP/blob/main/clip/model.py).

Similarity search can be retained for the library. The next component to build is a store containing each image's normalized `encode_image` vector and file path. Encode the text query with `encode_text`, then rank images by cosine similarity. This uses the documented vector-comparison mechanism. [API and normalization example](https://github.com/openai/CLIP). Relevance must be checked on your own library; the original model card says that languages other than English were not intentionally trained or evaluated. [Model card](https://github.com/openai/CLIP/blob/main/model-card.md).

I read the documentation and relevant code here. The model was not run, packages were not installed and weights were not downloaded.

## evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "embeddings",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "The official CLIP ViT-B/32 encodes supplied images and texts into vectors. Its forward returns similarities between the image and supplied texts, while the example calculates probabilities for texts specified in advance. This model and example have no decoder for freely generating image descriptions. Under the stated conditions, it therefore does not produce a complete new descriptive sentence.",
  "next_step": "For an image library, store each file's normalized encode_image vector and path; encode a text query with encode_text and rank images by cosine similarity between the vectors. A free-form descriptive sentence would require a different or additional trained component with a text-generation decoder, so the original constraint would have to change. The model was not run here.",
  "sources": [
    "https://github.com/openai/CLIP",
    "https://github.com/openai/CLIP/blob/main/clip/model.py",
    "https://github.com/openai/CLIP/blob/main/model-card.md",
    "https://github.com/openai/CLIP/blob/main/LICENSE",
    "https://github.com/openai/CLIP/blob/main/requirements.txt"
  ]
}
```

## baseline / IT03-dinov2-retrieval

**DINOv2 `ViT-S/14` provides an image representation that can support this search without training a new base model.** The authors' model card explicitly lists nearest-neighbour image retrieval; the ViT-S vector has 384 elements. Class labels are unnecessary for ranking image vectors against one another. [Model card](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

The sources include model code, weight links and an example loading `dinov2_vits14`. `forward_features` supplies the global `x_norm_clstoken` and local image-patch features; the ordinary `forward` returns the global representation through an `Identity` head. [Repository](https://github.com/facebookresearch/dinov2), [model code](https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py).

To build a search tool for your folder, the following processing still needs to be implemented:

1. Prepare local loading of the code and previously downloaded weights. The base-model loading code also accepts a weights path. [Loading code](https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py).
2. Process all images consistently, obtain global vectors, apply L2 normalization separately, and store the vectors with file paths.
3. Calculate the same kind of vector for the submitted image, rank the library by cosine similarity, and return the chosen number of nearest results.
4. Add image submission and result display, then check relevance on your own examples. These are application-processing steps around the documented nearest-neighbour mechanism. [Model uses](https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md).

The choice is therefore `adapt_output`. Result quality still needs checking on your folder: a project user reported poorer retrieval after cropping an image; that is a report of a specific experience. [Discussion](https://github.com/facebookresearch/dinov2/issues/103). I did not run inference, install packages or download weights here.

## evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": true,
    "native_output_kind": "embeddings",
    "action": "adapt_output",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "DINOv2 ViT-S/14 provides an image representation with 384 elements, and the authors' model card documents nearest-neighbour image retrieval without further adaptation of the base model. The code exposes the global x_norm_clstoken and patch features. The published base model is a usable component; a personal folder still needs indexing, similarity ranking and an image-submission interface. These steps do not require a newly trained base model.",
  "next_step": "Prepare local loading of the repository and weights. With consistent preprocessing, obtain each library image's global 384-element vector, apply L2 normalization separately and store it with the file path. Obtain the same kind of vector for the submitted image, calculate cosine similarity, select the top-k files and display them in the interface. Before wider use, check relevance on examples from your folder, including rotated images. No execution was performed here.",
  "sources": [
    "https://github.com/facebookresearch/dinov2",
    "https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py"
  ]
}
```

## candidate / IT01-depth-output

## Conclusion

The unit **m** must not be attached to this checkpoint's output. `depth-anything/Depth-Anything-V2-Small-hf` produces a relative-depth map. The model card labels it relative, and the authors' repository associates this specific Transformers example with the relative base models. The card's broader discussion of absolute-depth results does not establish a metre scale for this checkpoint.

The component can be retained for a relative **nearer/farther ordering** of image regions. An adapter can resize the map, display it or read values from a selected region. These operations do not recover the missing physical scale; the author also requires true metric-depth values to adjust the scale. This conclusion applies to the stated conditions, which provide no such reference measurements.

If an estimated metric-depth map is needed without training a model yourself, the next step is to select the authors' published metric Small checkpoint: Hypersim for indoor scenes or Virtual KITTI 2 for outdoor scenes. Its example specifies output in metres. This changes the checkpoint (`replace_core`); accuracy for the particular scene still needs checking.

I checked documentation, configuration and output-head code here. The model was not run, weights were not downloaded and no installation was performed.

## evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "relative_depth",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "depth_ordering"
  },
  "explanation": "The specific depth-anything/Depth-Anything-V2-Small-hf checkpoint produces a relative-depth map without a justified scale in metres. The card's broader discussion of absolute depth concerns the model family; the authors' repository separates relative base checkpoints from specially adapted metric models. Interpolation or normalization does not add metric scale.",
  "next_step": "Retain this checkpoint for relative nearer/farther ordering. If an estimated metric-depth map is needed without training a model yourself, replace it with the authors' published metric Small checkpoint: Hypersim for indoor scenes or Virtual KITTI 2 for outdoor scenes, and check its error under the conditions of your own scene. This changes the checkpoint; the originally fixed Small-hf cannot perform the requested function.",
  "sources": [
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf",
    "https://huggingface.co/depth-anything/Depth-Anything-V2-Small-hf/blob/main/config.json",
    "https://huggingface.co/docs/transformers/model_doc/depth_anything",
    "https://github.com/DepthAnything/Depth-Anything-V2",
    "https://github.com/DepthAnything/Depth-Anything-V2/blob/main/metric_depth/README.md",
    "https://github.com/huggingface/transformers/blob/v5.22.2/src/transformers/models/depth_anything/modeling_depth_anything.py",
    "https://github.com/DepthAnything/Depth-Anything-V2/issues/200",
    "https://github.com/LiheYoung/Depth-Anything/issues/226"
  ]
}
```

## candidate / IT02-clip-generation

## Conclusion

**No.** The official CLIP `ViT-B/32` and its published example do not produce a free-form image-description sentence. `encode_image` and `encode_text` return feature vectors, while `model(image, text)` returns similarities between an image and texts supplied in advance. The code's `forward` function also ends with those similarity tensors. The output family is `embeddings`.

An adapter can select the most suitable previously written sentence from a bank of candidates. It still chooses one of the supplied texts. A newly generated free-form description requires an image-captioning model with a trained text generator, or the addition of such a component. Under the task's definition, this is `replace_core` and requires changing the original constraint.

CLIP can be retained for **similarity search** in an image library. The next practical step is to store image vectors from `encode_image` with their file paths, encode an English query with `encode_text`, and rank images by similarity between normalized vectors. This is an adapter around the existing model and does not require training a new base model. It is a recommendation for using the documented functions; results on your own collection still need checking. An English query respects the language scope of the original model card.

I read documentation and code here. The model was not run, nothing was installed and model weights were not downloaded.

## evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": false,
    "native_output_kind": "embeddings",
    "action": "replace_core",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "The official CLIP ViT-B/32 encodes an image and previously supplied text into feature vectors. model(image, text) returns similarity logits, and the example chooses between text options supplied in advance. encode_text is not a sentence-generation decoder; this model and example do not produce new free-form image descriptions.",
  "next_step": "Free-form descriptions require an image-captioning model with a trained text generator, or the addition of such a component, so the original constraint must change. Retain CLIP for library search: use encode_image to generate and store image vectors with file paths, encode an English query with encode_text, and rank images by similarity between normalized vectors. This search adapter does not require a newly trained base model; result quality must be checked on your own collection.",
  "sources": [
    "https://github.com/openai/CLIP",
    "https://github.com/openai/CLIP/blob/main/clip/model.py",
    "https://github.com/openai/CLIP/blob/main/model-card.md",
    "https://github.com/openai/CLIP/blob/main/LICENSE"
  ]
}
```

## candidate / IT03-dinov2-retrieval

## Conclusion

**Yes.** The published DINOv2 `ViT-S/14` provides an image representation suitable for this purpose. The model card specifies 384-dimensional vectors and explicitly lists nearest-neighbour image retrieval without further training of the base model. Class labels are unnecessary for comparing a query vector with collection vectors in this way.

The model weights and feature-extraction code are ready: `forward_features` returns `x_norm_clstoken` and image-patch features. For a simple search over whole images, I would start with the CLS vector. An adapter is still needed for the final function, so the choice is **`adapt_output`**. The base model does not need to change.

Next steps for the adapter:

1. Apply the same preprocessing to the folder images and query image, obtain CLS vectors and L2-normalize them.
2. Store the collection vectors with image-file paths.
3. Compare the query vector with the collection using cosine similarity and return `top-k` results.
4. Add an interface for selecting an image and viewing the ranked results.

These are proposed data-processing steps around the documented representation. Quality still needs checking on the particular collection; obtaining the model alone does not provide a finished file-library application.

For local use, prepare the repository code, dependencies and weights file beforehand. The current `dinov2_vits14` function accepts `weights` with a local file path; the code supports loading through that path. The model card and the inspected code header specify the Apache-2.0 licence.

I checked sources and code here. The model was not run, weights were not downloaded and offline operation was not practically tested.

## evaluation_fields

```json
{
  "decision": {
    "requested_function_supported": true,
    "native_output_kind": "embeddings",
    "action": "adapt_output",
    "executed_here": false
  },
  "reuse": {
    "useful_function": "similarity_retrieval"
  },
  "explanation": "The published DINOv2 ViT-S/14 provides an image-feature representation; the model card specifies a 384-dimensional output and explicitly supports image retrieval with nearest neighbors without fine-tuning. forward_features returns x_norm_clstoken and patch features. Class labels and new base-model training are unnecessary for this retrieval path, but the published backbone alone is not a finished search interface for the user's folder.",
  "next_step": "Build a local adapter: prepare the repository code, dependencies and ViT-S/14 weights file; load dinov2_vits14 with weights pointing to the local file. Preprocess the collection and query consistently, extract x_norm_clstoken, L2-normalize the vectors, store them with file paths, calculate cosine similarity and return the top-k images. Add image selection and a results interface; check quality on your own collection. The base model does not need to change.",
  "sources": [
    "https://github.com/facebookresearch/dinov2",
    "https://github.com/facebookresearch/dinov2/blob/main/MODEL_CARD.md",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/models/vision_transformer.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/backbones.py",
    "https://github.com/facebookresearch/dinov2/blob/main/dinov2/hub/utils.py"
  ]
}
```
