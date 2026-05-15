Now I have all the information I need. Let me carefully synthesize the final review, verifying each claim against the paper text.

---

## Summary

The paper proposes NeMal, a pipeline combining LLMs (Mistral, ChatGPT), text-to-image diffusion (fine-tuned SD1.5), and foundation models (SAM, CoralSCOP, VLMs) to generate synthetic marine images with pseudo labels, and produces MarineSynth — a dataset of over 4 million synthetic image-text pairs. The paper demonstrates that models trained on this synthetic data (optionally combined with few real images) can approach the performance of models trained on thousands of real images across classification, segmentation, and VLM tasks.

## Strengths

- **MarineSynth is the largest marine synthetic dataset to date (4M+ image-text pairs from 2,332 marine conceptions).** The scale and systematic construction (conception list → LLM-based text prompt generation → T2I synthesis → pseudo labeling) represent a substantial engineering contribution to a domain where data is scarce and expensive to collect. (Sec. 4.1, abstract)

- **Impressive reduction in human effort for classification is demonstrated.** Training on synthetic data combined with only 5 real images per category achieves 57.25% accuracy, nearly matching the Oracle model trained on 9,400 real images (57.83%). This 99.95% reduction in required real data directly supports the paper's core value proposition. (Sec. 4.1, Table 2)

- **Broad evaluation across three tasks with distribution-shift test sets.** The paper tests classification (IND/OOD/CLG sets with different distribution shifts), dense segmentation (coral reef with 400 real test images), and vision-language understanding (500 marine QA pairs), providing evidence that the synthetic data helps across diverse task types, not just in-distribution classification. (Sec. 4.1, 4.3, 4.4)

- **Modular pipeline design with replaceable components.** NeMal explicitly assembles LLMs, T2I models, and foundation models in a coherent framework where each component can be upgraded as better models become available — a practical design choice for a fast-moving field. (Sec. 3.2, Sec. 4.3–4.4)

## Weaknesses

### Fatal
None.

### Major

- **The central "never-ending" claim is not empirically validated; all experiments are single-pass.** The paper's title, abstract, and Sec. 3.2 repeatedly foreground "never-ending" learning as the core contribution. However, every experiment generates synthetic data in one round and evaluates a single training pass. Fig. 5 (left) shows accuracy saturating as more synthetic images are used, but this still uses one generation round with increasing sample count, not iterative re-training on newly generated data from an improved model. The paper describes the never-ending capability as something that "depends on the user requirements" and "theoretically" could be achieved (Sec. 3.2), yet presents it as a demonstrated contribution in the title and abstract. This is a significant gap between what is claimed and what is shown.

- **No experimental comparison against existing synthetic data methods, marine-specific or general-domain.** The paper cites marine simulators (Potokar et al., 2022; Xie et al., 2009) and general-domain synthetic data pipelines (DatasetDiffusion, DreamDA) in Related Work (Sec. 1, 2.2) but does not compare against any of them experimentally. The classification experiments (Table 2) only compare synthetic-trained models against an Oracle (real data) baseline. Without a comparison against, e.g., a model trained on Potokar et al.'s simulator outputs, DatasetDiffusion's pipeline, or standard real-data augmentation (AutoAugment), the claimed advantage over "existing methods" (Sec. 1) is unsubstantiated. The paper argues it is a "pioneering" work for the marine domain, but the lack of baselines makes it impossible to assess how much the specific T2I-based pipeline adds over alternatives.

### Minor

- **Segmentation evaluation lacks a key baseline to isolate CoralSCOP's contribution.** The paper generates pseudo labels for synthetic coral images using CoralSCOP (Zheng et al., 2024), a foundation model trained on real coral images, and then trains segmentation models on (synthetic image, CoralSCOP label) pairs. While no test-set contamination occurs (test labels are ground-truth from coral biologists), the experiment does not compare against directly applying CoralSCOP zero-shot to the real test images. Without this baseline, it is unclear whether the reported improvements stem from the synthetic training data or from CoralSCOP's pre-existing knowledge about coral morphology being distilled through the training process. (Sec. 4.3)

- **SD1.5 fine-tuning details are insufficient for reproducibility.** The paper states "We first construct our internal marine text-image data based on our marine conception list for fine-tuning" (Sec. 3.1.3) but does not specify what data was used (how many images, from what sources), the training procedure (learning rate, batch size, number of steps, LoRA vs. full fine-tuning), or hyperparameters. This makes it difficult for others to reproduce or build on the work.

- **Tension between "minimal human effort" claim and 100K human preference annotations.** The paper repeatedly claims "minimal human efforts on data collection and labeling" (abstract, Sec. 1, contributions) yet collects 100K binary preference judgments from 12 volunteers to train the image selector (Sec. 3.1.3). While 100K binary comparisons are far less effort than collecting and annotating real underwater images (which require specialized equipment), the claim of "ignorable" or "minimal" human effort overstates the case. The selector training is a non-trivial human annotation step that should be acknowledged as part of the pipeline's cost.

- **Single-run results without statistical significance.** Tables 2, 4, and 5 report point estimates without confidence intervals or significance tests. Given that the segmentation test set has only 400 images and the VLM QA set has 500 pairs, variance could be meaningful. This limits the reliability of comparisons between settings (e.g., 53.66 vs. 57.83 for pure synthetic vs. Oracle).

- **VLM experiments compare against original (unfine-tuned) VLMs rather than against fine-tuning on real marine data.** The paper fine-tunes MiniGPT4/LLaVa on synthetic marine data and compares against the original off-the-shelf versions. Since these general-domain VLMs likely have minimal marine knowledge, any marine-domain fine-tuning would trivially improve performance. A stronger baseline would be fine-tuning on real marine image-text pairs (if available) to isolate the contribution of synthetic data quality. (Sec. 4.4)

### Trivial
- None beyond parser artifacts.

## Nice-to-Haves
- An iterative "never-ending" experiment: run at least two rounds of generation → train → evaluate → generate → retrain → show improvement. Even a simple two-round proof of concept would substantiate the paper's central claim.
- Quality distribution analysis of synthetic images (e.g., what fraction of images are faithful to their text prompts, by prompt source).
- A standard real-data augmentation baseline (AutoAugment, RandAugment) for the classification experiments.
- Release of the dataset and code (currently promised but no repository details given — this is important for impact but not a reviewable weakness since the paper states intent to release).

## Removed Points
These points are flagged to be removed, treat them with caution:

- *Criticism about figures being absent/not visible* — Parser artifact, not a paper problem. The original PDF contains the figures.
- *Claim that the paper "does not contextualize the gap between Oracle and synthetic models"* — The paper explicitly reports 57.25 (5-shot+ChatGPT+Alt-texts) vs. 57.83 (Oracle) and states they are "comparable." This criticism is factually wrong.
- *Claim that the BLIP2† setting constitutes "data leakage" that invalidates the classification results* — The paper itself acknowledges this as "potential information leakage" (line 197) and separates BLIP2† results from the main findings. The real contribution uses Alt-texts and ChatGPT prompts, which do not access real images.
- *Several formatting/style nitpicks* — These are parser errors, not author errors.
- *Strength about "first systematic never-ending marine learning framework"* — This strength is retained but its force is qualified by the verified weakness that the "never-ending" aspect is untested.
- *Missing appendix/references criticisms* — These sections exist in the original submission but were stripped by the PDF parser.

## Novel Insights
The most interesting observation that emerges from synthesizing these reviews is that the paper's actual achievement (a working pipeline that achieves near-Oracle classification with ~99.95% less real data) is arguably stronger than its advertised contribution ("never-ending" learning). The single-pass results speak for themselves and do not need the never-ending framing to be impactful. The gap between what the paper sells (an iterative, continuous learning system) and what it delivers (a static synthetic data generator) may cost it credibility without adding evidentiary value. If the authors reframed the paper around the static pipeline and saved "never-ending" for future work with iterative experiments, the paper would be both more honest and harder to attack.

## Suggestions
1. **Reframe the paper to de-emphasize "never-ending"** as a demonstrated property. Either provide at least a two-round iterative learning experiment, or rename the system to something like "MarineSynth" and present the never-ending aspect as a design goal / future direction. Currently the framing attracts criticism that the actual experiments cannot satisfy.
2. **Add at least one experimental baseline against an existing synthetic data approach** — even a simple comparison against Potokar et al.'s underwater simulator outputs (for classification) or a standard augmentation baseline would significantly strengthen the paper's positioning.
3. **Acknowledge and include the CoralSCOP zero-shot baseline** in the segmentation experiments so readers can isolate the contribution of synthetic training data vs. the foundation model's prior knowledge.
4. **Specify the SD1.5 fine-tuning details** (data composition, hyperparameters, training procedure) to improve reproducibility.
5. **Add confidence intervals or error bars** to all main results, especially given the modest test-set sizes.
6. **Be transparent about the human annotation cost** — 100K preference pairs from 12 volunteers is a meaningful effort. Acknowledge it as part of the pipeline's setup cost.

## Score and Decision

The paper makes a real contribution: a large-scale synthetic marine dataset, a systematic pipeline demonstrating that synthetic T2I data can dramatically reduce real-data requirements, and multi-task evaluation. However, the central "never-ending" claim is unvalidated, the evaluation lacks critical baselines against existing methods, and several methodological gaps weaken the evidence. The core results (near-Oracle accuracy with 5-shot synthetic data) are compelling, but the paper's framing overpromises relative to what is demonstrated.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>