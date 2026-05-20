Now I have all the information I need. Let me compose the final consolidated review.

---

## Summary

This paper identifies two gaps in standard ICL—*label appearance* (presence of labels in demonstrations) and *weak semantic relevance* (independently sampled demonstrations lack the coherence of pretraining text)—and proposes a method to perform ICL at the representation level using unlabeled test-set inputs. The approach extracts hidden states from each test input and retrieved unlabeled test samples, then reconstructs the test representation via attention-based mapping, using only an LLM's LM head for final prediction. Experiments across 8 datasets and 4 LLMs show consistent improvements over zero-shot and, in many settings, over traditional few-shot ICL that uses gold labels.

## Strengths

1. **Representation-level processing consistently outperforms text-level concatenation (Table 5).** Using the same unlabeled test-set inputs, all five mapping methods (attention, cosine, Pearson, Euclidean, Manhattan) improve over simple concatenation. For GPT-Neo-2.7B on SST2, gains exceed +20 points. This directly supports the core claim that independently processing demonstration representations mitigates weak semantic relevance better than standard concatenation.

2. **Preliminary analysis of the label-appearance gap (Table 2, Figure 1) is a genuine empirical contribution.** The controlled experiment removing labels from Topk-ICL reveals that labels hurt general-domain datasets (average Δ = +7.56 to +9.56 without labels) but help specific-domain datasets (average Δ = -10.62 to -21.16 without labels). This pattern is novel beyond prior work's focus on label shuffling and provides a principled explanation for when the proposed label-free method should work well.

3. **Consistent zero-shot improvements across model families (Table 4).** The method improves over zero-shot for all four LLMs (GPT-Neo-2.7B: +11.44%, Mistral-7B: +16.49%, Llama2-7B: +17.06%, Llama2-13B: +12.84%) across 8 datasets. Many gains are large (e.g., +42.45 on ACL for GPT-Neo-2.7B), and small models with the method surpass larger models' zero-shot performance (GPT-Neo-2.7B + method exceeds Llama2-7B zero-shot; Llama2-7B + method exceeds Llama2-13B zero-shot).

4. **Systematic ablation across pooling strategies reveals model-family differences (Table 7).** GPT-Neo-2.7B benefits most from *last-layer* pooling while Mistral-7B, Llama2-7B, and Llama2-13B benefit from *first-last* pooling. This cross-model analysis provides actionable guidance beyond typical single-model ablations.

## Weaknesses

### Fatal
None.

### Major

1. **Hyperparameters selected directly on the test set without validation (Section "Implementation Details", lines 230–231).** The paper states: "We initially set k = 64, τ = 1 to identify the optimal pooling strategy. Following that, we adjust the value of k, and finally, we tweak the value." No held-out validation split is mentioned for any of the 18 hyperparameter combinations (3 pooling strategies × 3 k-values × 2 temperatures). Because the method uses other test samples as retrieval candidates, the test set is already involved in the computation, and tuning on it means the reported numbers do not represent an unbiased estimate of generalization. The extent of overfitting is likely mild given the small hyperparameter space and the large, consistent gains, but the omission is a clear departure from standard evaluation practice. The fix is straightforward: hold out a portion of the test set for tuning, or use cross-validation within the test set.

2. **The architecture-level comparison with traditional ICL (Table 6) is between asymmetric data sources.** The proposed method uses unlabeled texts from the **entire test set** (minus the query), while the ICL baselines use 16 labeled examples from the **training set**. The paper is transparent about this (captions and Section 4.1 both note the difference), and the finding that unlabeled test-set information can sometimes be more useful than labeled training-set information is genuinely interesting. However, the abstract and introduction claim the method "outperforms traditional ICL with extra information of gold labels" without adequately discussing this fundamental asymmetry. The fairest comparison is Table 5, which compares text-level vs. representation-level processing on the **same unlabeled test data**, and it clearly supports the method. The stronger claim in Table 6 is inherently a comparison of two different paradigms and should be framed with corresponding nuance.

### Minor

3. **No statistical variance or error bars reported.** The paper uses a single random seed (42) and does not report standard deviations or confidence intervals (beyond p-values in Table 4, whose test is not specified). For classification with deterministic inference (BM25 retrieval + fixed model weights), the proposed method's output is deterministic, so multiple runs would not add variance. However, the ICL baselines—especially Random-ICL—have inherent randomness, and the lack of error bars on their scores makes it impossible to assess whether the reported improvements are statistically significant. This is standard practice for many ICL papers, but reporting it explicitly would strengthen the paper.

4. **Several design choices are introduced without justification (Section 3, Equation 11).** The fixed weights 0.4/0.6 in the weighted sum of retrieved and original representations, the L2 normalization (Equation 12), and the use of BM25 for retrieval (rather than the LLM's own representations) are presented without ablation or motivation. While these choices are not individually unreasonable, their ad-hoc nature weakens the sense of principled design. An ablation on the weight parameter or a brief justification for each choice would help.

5. **The connection between the toy analysis (Section 2.3, Equations 3–4) and the final algorithm is loose.** The analysis compares self-attention on concatenated sequences vs. separate self-attention + cross-attention for a single layer with m=1. The actual method uses pooled representations from all layers with a separate attention computation, not the LLM's internal cross-attention. The analysis provides useful intuition but does not directly analyze the proposed algorithm.

### Trivial
None worth listing.

## Nice-to-Haves

- **Analyze the effect of the task description** that mentions label names (e.g., "positive or negative"). An ablation without this description would measure how much the method relies on label-space leakage.
- **Quantify the computational overhead** (extra LLM forward passes for retrieving and processing k samples) relative to zero-shot or standard ICL. The limitations section mentions latency but does not provide numbers.
- **Include a discussion of transductive vs. inductive evaluation.** The method is by nature transductive, and acknowledging this framing explicitly would contextualize the comparison with inductive ICL baselines.
- **Run a larger model (e.g., Llama2-70B)** to test whether the advantage over zero-shot holds at scale, though the current 4-model range (2.7B to 13B + API) is already reasonable.

## Removed Points

The following points from the input reviews were removed with justification:

- **"Unfair comparison with ICL (fatal framing)"** — The harsh critic framed Table 6 as fundamentally unfair. The paper is transparent about the asymmetric setting, and the comparison is interesting precisely *because* it crosses paradigms. Demoted from what the critic called "structural" to Major/concern-about-claim-framing.
- **"Reproducibility concern about BM25 implementation details"** — Removed per hard rules: missing implementation specifics (stopwords, stemming) for a standard retrieval algorithm are minor and typical of conference papers.
- **"No error bars" framed as fatally undermining all results** — The method is largely deterministic; the main missing error bars are on baseline variance. Demoted to Minor.
- **"Missing related works"** — Removed per hard rules (cannot verify without external sources).
- **"Limited model size range"** — 4 models from different families (GPT-Neo, Mistral, Llama2, GPT-3.5) is reasonable.
- **"No discussion of transductive nature"** — The paper does implicitly acknowledge this by repeatedly stating it uses "unlabeled texts from the test set"; a more explicit framing would be nice-to-have.
- **Generic strengths from Strength Finder** — Strengths that were generic or sycophantic (e.g., "this paper addresses an important problem") have been dropped; only concrete, evidence-grounded strengths remain.

## Novel Insights

The harsh critic and strength finder both identify the same useful tension: the paper has a genuinely novel idea (representation-level ICL with unlabeled test inputs) supported by strong preliminary analysis (label-appearance gap), but the evaluation protocol has a significant methodological gap (test-set hyperparameter tuning). Neither reviewer surfaces a deep conceptual flaw beyond this evaluation concern. The most interesting observation is that the label-appearance analysis (Table 2) could stand as a contribution on its own—it cleanly separates general-domain and specific-domain datasets and provides a principled criterion for when label-free ICL is feasible, which is actionable for practitioners.

## Suggestions

1. **Add a validation split.** Reserve 20% of each test set for tuning (pooling, k, τ) and report results on the remaining 80%. Given the small hyperparameter space (18 combinations), this is feasible even on datasets as small as RTE (277 samples) and ACL (139 samples). Report both the tuned and full-test results with appropriate caveats.

2. **Reframe the comparison with traditional ICL.** Add a sentence to the abstract and introduction clarifying that the comparison in Table 6 is between the proposed transductive method (using unlabeled test inputs) and standard inductive ICL (using labeled training examples). Keep the Table 6 results but add a parallel comparison where both methods use the same test-set data (which is already done in Table 5—make this the primary "method comparison" table).

3. **Ablate the 0.4/0.6 interpolation weight** (Equation 11) over a range (e.g., 0.0 to 1.0) to show sensitivity.

4. **Run Random-ICL baselines with multiple seeds** (e.g., 5) and report mean ± std to provide variance estimates.

5. **Move the toy analysis (Section 2.3) to the appendix** or explicitly connect each step of the analysis to the corresponding design choice in Section 3, clarifying that it illustrates intuition for a simplified case (single layer, m=1) rather than analyzing the full algorithm.

## Score and Decision

**Calibration Protocol:**

**Round 1 (Bracketing):** Three queries across score bands on topics in ICL, representation-level methods, and unlabeled/test-set adaptation.

*Low band (< 3.5)*: Anchors at ~3.0 (e.g., "On Unsupervised Prompt Learning" avg 3.0, "Fine-Grained Emotion Recognition with ICL" avg 3.0). These papers have limited experiments, unclear methodology, or poor writing. The paper under review is clearly stronger.

*Middle band (3.5–7.5)*: Anchors include "How does representation impact ICL" (avg 4.5, rejected), "ICLR: In-Context Learning of Representations" (avg 6.5, accepted poster), "How Do Transformers Learn In-Context Beyond Simple Functions" (avg 6.5, accepted poster), "From Context to Concept" (avg 6.0, rejected), "Unsupervised ICL" (avg 5.75, accepted poster), "Supervised Knowledge Makes LLMs Better ICL" (avg 5.0, accepted poster).

*High band (> 7.5)*: Anchors at 8-9 (accepted oral/poster). The paper under review does not reach this level.

**Round 1 Bracket:** The paper sits in the 4.5–6.5 range.

**Round 2 (Narrowing):** Two queries within the bracket.

Anchors narrowed to: "Supervised Knowledge Makes LLMs Better ICL" (avg 5.0, accepted) — this paper has a simple but effective idea with good experiments but limited novelty; the paper under review has stronger novelty but a more significant evaluation concern. "Unsupervised ICL" (avg 5.75, accepted) — similar unsupervised-adaptation framing; the paper under review is slightly weaker in evaluation rigor but comparable in contribution. "Which Examples to Annotate" (avg 4.25, rejected) — has unconvincing claims and limited novelty. "Disentangling Latent Shifts of ICL" (avg 5.75, rejected due to one low score) — interesting idea but with framing concerns.

The paper under review is:
- **Stronger than** avg 4.25 (rejected) and avg 4.5 (rejected) papers (better experiments, clearer contribution)
- **Comparable to** avg 5.0 (accepted) papers (similar novelty level, similar experimental breadth)
- **Weaker than** avg 6.5 (accepted) papers (those have stronger theoretical grounding or more rigorous evaluation)

The paper's main liability is the test-set hyperparameter tuning, which is a significant methodological oversight but not fatal given the large, consistent gains and small hyperparameter space. The idea is genuinely novel and the experiments are broad (8 datasets, 4 LLMs). The paper is slightly below the acceptance threshold in its current form but could be strengthened.

**Final Score:** 5.0

**Decision:** Reject

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>