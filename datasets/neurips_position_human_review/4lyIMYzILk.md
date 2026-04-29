# Deepfakes: we need to re-think the concept of “real” images

- Decision: Reject
- Scores: 5, 4, 7

## Abstract
The wide availability and low usability barrier of modern image generation mod-
els has triggered the reasonable fear of criminal misconduct and negative social
implications. The machine learning community has been engaging this problem
with an extensive series of publications proposing algorithmic solutions for the
detection of “fake”, e.g. entirely generated or partially manipulated images. While
there is undoubtedly some progress towards technical solutions of the problem,
we argue that current and prior work is focusing too much on generative algo-
rithms and “fake” data-samples, neglecting a clear definition and data collection
of “real” images.

The fundamental question *“what is a real image?”* might appear to be quite
philosophical, but our analysis shows that the development and evaluation of
basically all current “fake”-detection methods is relying on only a few, quite old
low-resolution datasets of “real” images like ImageNet. However, the technology
for the acquisition of “real” images, aka taking photos, has drastically evolved
over the last decade: Today, over 90% of all photographs are produced by smart-
phones which typically use algorithms to compute an image from multiple inputs
(over time) from multiple sensors. Based on the fact that these image formation
algorithms are typically neural network architectures which are closely related to
“fake”-image generators, we state the position that today, **we need to re-think
the concept of “real” images**.

The purpose of this position paper is to raise the awareness of the current short-
comings in this active field of research and to trigger an open discussion wether
the detection of “fake” images is a sound objective at all. At the very least, we
need a clear technical definition of “real” images and new benchmark datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This position paper argues that current efforts in detecting fake/generated images neglect a critical issue: the lack of a clear and contemporary definition of “real” images. It highlights that most benchmark datasets used to train detection algorithms are outdated, low-resolution, and unrepresentative of modern imaging pipelines—particularly those produced by smartphone devices using image enhancement algorithms. Through a series of empirical evaluations and conceptual analysis, the authors call for a redefinition of what qualifies as “real” imagery, better datasets, and even question whether detection-based approaches are ultimately viable. The paper’s goal is to spark discussion and reflection in the NeurIPS community about foundational assumptions in deepfake detection research.

### Strengths
The paper challenges a widely held assumption in the deepfake detection community and raises a critical philosophical and practical issue. The four propositions are logically structured and well supported by experimental evidence and data analysis. The position is novel, timely, and of clear importance to both the machine learning and computer vision communities. The conclusion offers actionable insights, including the need for dynamic “real” image datasets and the reconsideration of semantic “realness” rather than technical authenticity.

### Weaknesses
The experimental evidence, while illustrative, is based on a limited sample (iPhone RAW images and LAION metadata) and may not be fully generalizable. The philosophical discussion could be more rigorous, and the paper does not engage deeply with other domains (e.g., legal, media theory) that have addressed notions of authenticity. Alternatives like watermarking are briefly mentioned but not analyzed in depth. Finally, there are some minor issues in phrasing and formatting throughout the paper.

### Questions
Could the authors elaborate on what criteria would be acceptable for defining "semantic authenticity" in images across domains (e.g., journalism, social media, surveillance)?

How do the authors envision building a community-curated, privacy-preserving dataset that adapts to evolving imaging technology?

Is there potential to learn "realness" as a latent concept from user-annotated data instead of defining it a priori?

### Presentation
3

---

## Human Reviewer 2

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
The position asserts that the current deepfake research domain is narrow in detection with the main recommendation being “rethinking” of strategy to include provenance tracking, watermarking, public awareness and multi-stakeholder collaboration.

### Strengths
S1: The position highlights a real-world, existing problem that detection lags behind generation. 
S2: The authors frame the discussion as a societal harm, highlighting the importance of addressing this challenge.

### Weaknesses
W1: The discussion on legal and ethical trade-offs reads superficial, and a deeper discussion on this would be more useful for the position.
W2: The authors can include some new technical insights made through the position taken in this paper.
W3: The authors can include some statistics to provide evidence on the examples cited in the paper, such as detection accuracy trends.

### Questions
See weaknesses.

### Presentation
3

---

## Human Reviewer 3

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
The paper is a position piece arguing that progress in image deepfake detection is constrained not by the sophistication of generative models alone, but by an outdated and underspecified notion of what counts as a “real” image. The authors claim that most detection benchmarks rely on a small set of old, low-resolution “real” datasets (e.g., ImageNet, LSUN, CelebA), while the vast majority of photographs today are produced by smartphone pipelines that algorithmically compute imagery via multi-frame fusion and neural enhancement—processes that blur the boundary between “captured” and “generated.”

### Strengths
Well-articulated diagnosis of a real failure mode: detectors trained on stale “real” distributions may not generalize. The cross-check of Re-LAION-5B’s recency and resolution distribution (via EXIF and size histograms) is informative.

The survey table makes visible the limited diversity of “real” sources used by many benchmarks.

### Weaknesses
Empirical support is preliminary: the EXIF-based analysis is confined to iPhones as a proxy, and the proof-of-concept detector tests are small-scale (the paper itself notes the need for a “full-scale study”).

No concrete protocol for collecting, curating, and refreshing “real” datasets is offered beyond high-level desiderata (privacy, dynamism, coverage).

The semantic redefinition of “fake” (harmful intent) is compelling but under-operationalized—how would benchmarks annotate “harm,” and at what unit (pixel, object, narrative)?

### Questions
Please specify a minimal viable “Real-2025” schema: device diversity (brands, models, lens types), capture contexts (lighting, HDR, burst, night modes), resolution policy (retain native full-res), metadata policy (EXIF preservation), and refresh cadence (e.g., quarterly device updates). Also outline a privacy pathway (face/license plate handling) that balances legal obligations with distributional fidelity—this tension is acknowledged but not resolved.

Demonstrate which on-device steps most confound detectors (e.g., multi-frame HDR, denoising, upscaling, Deep Fusion-style burst fusion). A modular study (simulate each step) would inform detector design and could suggest augmentation strategies for robustness.

### Presentation
3
