## Summary
The paper proposes the Fast and Slow Effect (FSE) framework to evaluate, without human supervision, whether LLM/VLM-generated concept annotations are *sufficient* for concept-based XAI. It introduces a Class Representation Index (CRI) that measures whether an LLM, given only its own staged textual concepts, can pick the correct class from 5 semantically-similar candidates ("slow mode") vs. seeing the image directly ("fast mode"). The headline finding is that on fine-grained datasets slow mode trails fast mode by ~25%, and "fused" mode tracks fast mode — used to argue that the utility-as-proxy assumption is misleading.

## Strengths
- The distractor-validation experiment (Table 1) shows semantically related distractors (ResNet-18 top-4 confusions) yield 34–45% contradiction vs. 14–20% for random distractors, providing concrete justification that the candidate set is non-trivial.
- The fused vs. slow contrast (Table 4) is a clean and informative finding: on fine-grained data, fused ≈ fast (~90%) while slow ≈ 50%, giving direct evidence that strong end-to-end accuracy can coexist with weak text-only supervision.
- Breadth across six models (GPT-4o/-mini, Llama-3.2-vision-90B/11B, Qwen-VL2-72B/7B) and five datasets covering both fine-grained (CUB-200, Cars-196, Flowers-102) and general (CIFAR-100, Caltech-101) recognition, in both post-hoc and visual-grounded modes.
- The granularity reversal on CIFAR/Caltech (Table 3, slow > fast at t=5) is a genuinely useful empirical observation that complicates the simple "annotations are insufficient" reading.

## Weaknesses

### Fatal
None — the concerns below are real but do not invalidate the framework outright.

### Major
- **Circular readout: the same model that generated the concepts also classifies from them (Eq. 2).** A low CRI cannot be cleanly attributed to insufficient annotations vs. a weak 5-way text classifier vs. concept-vocabulary/readout mismatch. Without (a) a decoupled readout (different LLM, or text-embedding linear probe) or (b) a gold-standard anchor — e.g., CUB human attributes (Welinder et al., already cited) evaluated under the same CRI protocol — the central verdict that "annotations are insufficient" cannot be isolated from readout quality.
- **Fast vs. slow conflates information modality with annotation sufficiency.** Fast mode has the image; slow mode has only a short textual concept chain — but distractors are *visually* selected (ResNet-18 top confusions). For pairs differing in cues that are hard to textualize at short length (e.g., subtle plumage textures in CUB), slow mode is penalized by construction. The "Slow Mode Superiority" hypothesis (§4.2) invokes Kahneman's dual-process theory but does not justify why a strictly-less-input condition should match an image-grounded one. A meaningful contrast would match input *length* across modalities (e.g., short caption vs. concept chain).
- **Internal coherence: the CIFAR/Caltech reversal cuts against the headline.** Table 3 shows the same pipeline yields "insufficient" on fine-grained and "sufficient" on coarse data. A more parsimonious reading is that CRI tracks textual separability of the candidate set, which scales with granularity — not annotation quality alone. The paper notes the reversal but still concludes annotations "struggle to externalize implicit expertise"; it does not engage the alternative interpretation.

### Minor
- **Eq. 2 normalization error.** CRI is written as $\frac{1}{t}\sum_{i=1}^{t} \mathbb{1}[y_i^t=y_i]$, where $t$ is both the annotation-step index and the sum's upper bound. This should be $\frac{1}{N}\sum_{i=1}^{N}$ (or $|\mathcal{D}_\text{test}|$). The Eq. 1 union $\bigcup_{j=1}^{t-1}$ also yields $c_i^1=\emptyset$, inconsistent with the description that t=1 produces the Background stage.
- **Non-monotonic CRI trajectory unexplained.** Table 3 shows GPT-4o CRI at t=1 on fine-grained avg is 27.67 — below random chance (20% for 5-way is the floor; 27% is essentially at chance), and t=2 (27.11) is *lower* than t=1. The "concept-chain" framing implies monotone refinement; the early stage appears to actively harm prediction, and this is not analyzed.
- **No distractor-source ablation.** ResNet-18 is a weak backbone whose confusion structure may not reflect VLM or human confusions. Comparing distractor sources (random / ResNet / CLIP / textual-similarity) would substantively clarify what CRI measures.
- **Utility-as-proxy conclusion overreaches.** Fused matching fast shows text adds little marginal value over the image on these benchmarks; concluding utility-as-proxy is *generally* unreliable is a broader claim than the evidence supports.
- **§8 Limitations does not engage** modality asymmetry or readout/annotator coupling — the two largest structural concerns about the framework.

### Trivial
None retained.

## Nice-to-Haves
- Anchor CRI with human/expert annotations (CUB has expert attributes) under the same protocol.
- Decouple readout from annotator: a different model, or a non-LLM classifier over concept embeddings.
- Treat the granularity reversal as a primary contribution: characterize *when* text-based concept supervision works and when it does not.

## Removed Points
*These points are flagged to be removed; treat them with caution.*
- "Clear formal definition of sufficiency (Def 3.1)" as a strength — too generic to distinguish this paper.
- "Five-stage process grounded in prior work" — descriptive of design, not evidence of contribution quality.
- Reviewer suggestions about Appendix B prompt design and reproducibility/appendix details — appendix-stripped artifacts.
- Harsh critic's "distractor protocol biases slow mode downward" framed as separate — merged into the modality-asymmetry weakness to avoid double-counting.

## Novel Insights
The reviews together surface one synthesis worth flagging: the framework's verdict on "annotation sufficiency" appears to track the *textual separability of the candidate set* (a function of dataset granularity and the ResNet-conditioned distractor construction) more than properties of the annotations themselves. The CIFAR/Caltech reversal, the visually-selected distractors, and the annotator-as-readout coupling jointly imply CRI is best read as a joint measure of (annotation expressiveness × readout quality × text-discriminability of distractors). Reframing the paper around this decomposition would be more defensible than a single-axis claim.

## Suggestions
- Add a human/expert-annotation upper bound for CRI on CUB.
- Add an ablation over distractor source (random/ResNet/CLIP/text-similarity).
- Decouple the readout LLM from the annotator LLM in at least one experiment.
- Diagnose why t=1 CRI is at or below chance on fine-grained data.
- Fix Eq. 1 union indexing ($j=1,\ldots,t$) and Eq. 2 normalization ($N$, not $t$).
- Promote the granularity reversal to a primary finding and analyze its mechanism.

## Calibration

Anchors retrieved:
- **Round 1 (bracketing)**:
  - `KLUDshUx2V.md` (avg 3.40, reject): essentially the same topic — LLMs generating concept banks for CBMs with a new evaluation metric. Most directly comparable.
  - `kTjEPEy96Q.md` (avg 3.00, reject): evaluation framework for unsupervised CBMs.
  - `wZiH43e5Ah.md` (avg 3.00, reject): concept extraction framework.
  - `J0qgRZQJYX.md` (avg 3.00, reject): axiomatic concept explanations.
  - `0qrTH5AZVt.md` (avg 4.67, reject): ConLUX concept-based explanations.
  - `RC5FPYVQaH.md` (avg 5.75, accept): Concept Bottleneck LLMs — more methodologically substantive.
  - `TdyfmCM8iR.md` (avg 4.33, reject): latent concept NLP explanation.
  - `Ba5KGabRe8.md` (avg 4.25, reject): XplainLLM QA explanation dataset.
  - `WbWtOYIzIK.md` (avg 8.00), `GGlpykXDCa.md` (avg 8.00), `I4e82CIDxv.md` (avg 8.00), `z8sxoCYgmd.md` (avg 8.00): high-scoring papers, but topically distant.
- **Round 2 (narrowing)**:
  - `KLUDshUx2V.md` (3.40) again — confirmed as closest analog.
  - `Q9Z0c1Rb5i.md` (avg 5.00, reject): hierarchical CBM with information leakage analysis — more methodologically complete than this paper.
  - `5Aem9XFZ0t.md` (avg 4.83, reject): zero-shot CBMs via sparse regression.
  - `uuvujfQXZy.md` (avg 4.33, reject): selective CBMs without predefined concepts.
  - `kZEXgtMNNo.md` (avg 6.00, accept): LLMs as automated aligners for VLM benchmarking — comparable evaluation-framework angle, but with stronger methodology.
  - `fO1xnmW8T6.md` (avg 4.25, reject), `ZuYvrjh2od.md` (avg 5.00, reject).

Round-1 bracket: between 3 and 5.5, closest to the 3.4 anchor.
Round-2 narrowing: the paper is somewhat more thorough in experimental breadth than `KLUDshUx2V` (3.40) but suffers from a more conspicuous methodological coupling (the annotator-as-readout circularity, plus the modality asymmetry that the framework's headline claim hinges on). It is below `Q9Z0c1Rb5i` (5.00) and `kZEXgtMNNo` (6.00), which have better-isolated methodological claims. It is at or just above `KLUDshUx2V` (3.40).

Final placement: 4.0 — slightly above the closest analog (3.4) to credit broader experiments and the interesting CIFAR/Caltech reversal, but well below the 5.0-tier anchors because the central empirical claim has multiple unaddressed alternative explanations.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>