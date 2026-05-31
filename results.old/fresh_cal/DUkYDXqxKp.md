Now I have all the information needed. Let me write the final consolidated review.

---

## Summary

DriveGPT4 is a multimodal LLM for interpretable end-to-end autonomous driving. It takes multi-frame video from a monocular camera and produces both natural-language explanations (action descriptions, justifications, open-ended Q&A) and low-level control signals (speed, turning angle) in a single autoregressive pass. The key ideas are: (1) treating control signals as text tokens so the LLaMA tokenizer handles both language and numerical outputs, (2) creating a 56K driving-specific instruction-tuning dataset via ChatGPT with privileged information (object detections, control signals, captions), and (3) a mix-finetuning strategy that jointly trains on domain-specific (56K) and general visual instruction data (223K). Evaluations on BDD-X show text-generation improvements over ADAPT and general video-LLM baselines, and ablations validate the importance of each design component.

---

## Strengths

- **Mix-finetuning strategy with strong ablation evidence.** The ablation study (Table 6) directly validates that combining domain-specific and general instruction data is critical: removing the mix-finetune step drops CIDEr from 99.10 → 76.51 on BDD-X QAs and increases speed RMSE from 1.30 → 4.67. This is controlled evidence that both data sources are necessary, not just a single design choice.

- **Unified text+control tokenization is a concrete architectural contribution.** DriveGPT4 uses the LLaMA tokenizer and de-tokenizer for both natural language and numerical control signals (inspired by RT-2), enabling joint generation of interpretations and controls in a single autoregressive pass. This differs from prior work like ADAPT which uses separate heads for text and cannot natively predict controls.

- **Creation of a domain-specific instruction-tuning dataset.** The paper generates 40K ChatGPT-assisted multi-turn Q&A pairs about driving scenes (beyond the 16K BDD-X QA pairs), addressing the lack of diverse instruction data for autonomous-driving language tasks. Ablations confirm these data are essential: removing ChatGPT QAs drops the ChatGPT evaluation score from 81.62 → 31.03.

- **Structured evaluation across difficulty levels.** The BDD-X test set is split into Easy/Medium/Hard based on scene complexity. DriveGPT4 outperforms all baselines on every split, with the largest margins on Hard scenes (CIDEr 57.29 vs. ADAPT's 52.71 for full-text QA). This provides stronger evidence than a single aggregate score.

- **Clear text-generation improvements on BDD-X.** DriveGPT4 achieves CIDEr 99.10 vs. ADAPT's 85.38 on full-text generation, with consistent gains on description and justification subtasks. These results use BDD-X's human-annotated ground truth, not ChatGPT-generated references, and are not subject to the circularity concern discussed below.

---

## Weaknesses

### Fatal

None.

### Major

- **The ADAPT baseline for control signal prediction is unsubstantiated.** Table 4 reports that ADAPT achieves speed RMSE=3.02 and turning-angle RMSE=11.98. ADAPT (Jin et al., 2023) is a language-based interpretability method that predicts action descriptions and justifications — it is not designed to predict low-level control signals, and the paper provides no explanation whatsoever of how ADAPT was adapted to output speed and steering values. The paper states "All methods are required to predict control signals for the next time step" (Section 5.2) without describing any modification to ADAPT. Without knowing whether ADAPT was given a linear regression head, fine-tuned with a control loss, or some other adaptation, it is impossible to interpret the claimed superiority. The comparison is methodologically unreliable, and the control-prediction claims (which are part of the core "end-to-end" contribution) rest on it. The ablation studies (Table 6) still provide valid self-comparison evidence, but the headline control results versus the "SOTA baseline" are not credible as presented.

- **The ChatGPT-based evaluation of additional QAs is circular.** For the "Additional Question Answering" experiments (Table 4), ChatGPT both generates the questions/answers (using privileged information from BDD-X test videos) and scores DriveGPT4's outputs. This creates a feedback loop: the model is trained to mimic ChatGPT's style, and ChatGPT then assigns higher scores to outputs that match its own prior. The conventional NLP metrics (CIDEr, BLEU4, ROUGE) reported alongside are not independent either, since they compare against ChatGPT-generated ground-truth answers. The paper acknowledges the ChatGPT score's instability (line 369: "the ChatGPT score is not stable, thus we report the mean of three times of evaluations") but does not address the deeper validity concern. This evaluation does not reliably measure interpretability or correctness — it measures stylistic agreement with the teacher model. Notably, this issue is confined to the "Additional QA" experiments; the main BDD-X QA results (Tables 2, 3) use human-annotated ground truth and are not affected.

### Minor

- **LLaMA2 model size is not specified.** The paper states "In this paper, LLaMA2 is adopted as the LLM" (line 177) without indicating the variant (7B, 13B, or 70B). This matters for reproducibility and for assessing whether text-generation gains might partly reflect larger model capacity rather than the proposed method. Since Video-LLaMA and Valley also use LLaMA/Vicuna, the scale may be comparable, but the omission makes this impossible to verify.

- **Testing set split criteria are not formally defined.** Table 1 lists example scenes for Easy/Medium/Hard splits ("Stopped; Driving forward; Parked" etc.) but provides no formal rule or algorithm for assignment. This makes the split non-reproducible and the "Hard" improvement claims harder to interpret independently.

- **Zero-shot generalization results are qualitative only.** Figures 8 and 9 show examples on NuScenes and video-game footage but provide no quantitative evaluation (e.g., no human-rated accuracy, no control signal RMSE on these domains). As presented, these serve as anecdotes rather than evidence of generalization.

- **GPT4-V comparison (Figure 10) is a single qualitative example.** DriveGPT4 is compared against GPT4-V on one example, where GPT4-V fails to predict control signals and misidentifies dynamic actions. This is expected given that DriveGPT4 is fine-tuned on driving data and GPT4-V is a general model. A single example does not constitute a meaningful comparison.

- **Ablation table (Table 6) is confusingly presented.** The first row (no checkmarks for BQ, CQ, or MF) corresponds to Valley, but this is not labeled in the table itself — it is only implied by textual context. Dependencies between rows are hard to follow at a glance.

- **Training order (general data first, then domain data) is not ablated.** The paper mentions this ordering is used "for training efficiency" (line 214) but provides no experiment showing whether this order outperforms joint training or the reverse order.

### Trivial

None.

---

## Nice-to-Haves

- Add a small-scale human evaluation on the ChatGPT-generated questions to validate whether DriveGPT4's answers are actually accurate and natural, breaking the reliance on ChatGPT as both teacher and judge.
- For the control prediction claims, include baselines that are actually designed for control regression (e.g., a simple MLP, GRU, or trajectory prediction network) rather than relying solely on a retrofitted text-generation model.
- Clarify whether the dataset and prompt templates will be publicly released — these are a central contribution and would be valuable to the community.
- Consider providing quantitative zero-shot results on a small held-out set to support the generalization claims.

---

## Removed Points

These points were raised by reviewers but are removed from the main assessment (with justification):

- **"First to ground LLMs for interpretable end-to-end autonomous driving is undercut by concurrent work."** — Removed because the paper explicitly acknowledges DriveLM, DriveLikeHuman, and NuPrompt and draws clear, defensible distinctions (DriveLikeHuman: simulation-only; NuPrompt: object tracking only; DriveLM: a benchmark). The claim specifically refers to combining LLM-based interpretability with end-to-end control prediction on real-world driving data, which is distinct from the cited works.

- **"Missing training hyperparameters (learning rate, batch size, epochs, optimizer, hardware)."** — Removed per the instruction to discard nitpicks about undisclosed hyperparameters that are standard implementation details. The two-stage training procedure is described at a sufficient level (pretrain projector only, then fine-tune LLM+projector).

- **"The paper does not release the dataset or prompt templates."** — Removed per the instruction that criticisms questioning release status of cited/existing artifacts should be removed. The project webpage is provided.

- **"The scale comparison is unfair because DriveGPT4 uses more data."** — Demoted from Major to Minor and reframed as the model size specification issue. The data advantage (using general instruction data alongside domain data) is an intrinsic part of the method's contribution, not a confound. A fair comparison would compare the method with/without the general data (which the ablation does), not force the baseline to use the same data (which would change the baseline into a different method).

- **Strengths removed:** "Significant quantitative improvements on control signal prediction" is weakened by the invalid ADAPT baseline issue and is moved here rather than kept as a claimed strength. "Qualitative comparison showing advantages over GPT4-V" and "Zero-shot generalization" are removed as they rely on single-example qualitative evidence that does not constitute strong support.

---

## Novel Insights

None beyond the paper's own contributions. The two reviewers generally agreed on the paper's strengths and weaknesses; the main novel observation from synthesizing them is that the paper's core claims separate into two tiers: the text-generation contribution (supported by proper baselines and ablations, and only tangentially affected by the circular-evaluation issue on a subset of experiments) and the end-to-end control contribution (significantly weakened by the unexplained ADAPT control baseline). This distinction is important because it means the paper has a real, well-supported contribution (interpretable driving via mix-finetuned LLMs) alongside an evaluation gap on the control front that needs to be addressed.

---

## Suggestions

1. **Clarify or replace the ADAPT control baseline.** Either (a) explain exactly how ADAPT was modified to predict controls and argue why this is a meaningful comparison, or (b) drop the ADAPT comparison and instead include standard control-prediction baselines (e.g., a linear regressor, a simple RNN, or an end-to-end driving network like CILRS or LBC) to contextualize DriveGPT4's control performance.

2. **Add a human evaluation sample for the ChatGPT-generated QA experiments.** Select a subset of 50–100 outputs and have 2–3 human annotators rate accuracy/naturalness, reporting inter-annotator agreement. This would address the circular-evaluation concern.

3. **Specify the LLaMA2 variant used** (7B, 13B, or 70B) to improve reproducibility and enable fair interpretation of model capacity.

4. **Provide formal criteria or reproducible labels for the Easy/Medium/Hard test splits** so that future work can replicate the nuanced evaluation.

5. **Add quantitative zero-shot evaluation** on a small set of NuScenes or other driving-video clips with human-authored QA and control annotations.

---

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>