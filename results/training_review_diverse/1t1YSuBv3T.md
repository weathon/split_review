I have verified the paper content thoroughly against each reviewer claim. Here is the consolidated review.

---

## Summary

This paper proposes EATQA, a unified triplet generation framework that jointly trains an LLM on three complementary instruction-tuning tasks — answer-aware evidence generation (QA→E), evidence-enhanced question answering (QE→A), and evidence-aware question restoration (EA→Q) — plus a distribution-bridging KL regularizer that closes the gap between training (with evidence) and inference (without evidence). The method achieves state-of-the-art results on MultiRC (65.5 EM, 89.8 F1 with 13B, outperforming PaLM 540B) and Qasper (45.1 F1 with 7B), with strong ablations confirming each module's contribution.

## Strengths

- **Novel unified triplet generation framework with Bayesian motivation**: The paper jointly trains three tasks (QA→E, QE→A, EA→Q) grounded in a Bayesian decomposition (Eq. 1) that ties answer correctness to evidence extraction and question restoration. Ablations (Table 3) confirm each module contributes meaningfully — e.g., removing question restoration drops EM by 1.7 (7B) and 1.3 (13B); removing evidence generation drops EM by 2.1 (7B) and 1.0 (13B). The positive correlation among the three subtask scores (Figure 3) further validates that the framework captures logical relations among question, evidence, and answer.

- **Distribution bridging for train-inference gap**: The KL-divergence term (Eq. 2/4) distills evidence-grounded knowledge into the evidence-absent setting, enabling direct answer generation from the document at inference without an external retrieval step. Ablation (Table 3) shows removing this term drops EM by 0.9 on both 7B and 13B, confirming its practical value.

- **New state-of-the-art results on two challenging GQA benchmarks**: EATQA-13B achieves the best reported results on MultiRC (65.5 EM, 89.8 F1, Table 1), surpassing even PaLM 540B with statistical significance (p < 0.001). On Qasper, EATQA-7B reaches 45.1 F1 (Table 2), outperforming all prior LLM-based methods including those with larger backbones and long-context techniques.

- **Explicit hallucination mitigation analysis**: Table 4 measures two distinct dimensions — prior knowledge retention (P(Y_{A|Q}=Ŷ) improves from 34.8% to 37.1%) and hallucination reduction for unknown questions (P(Y_{A|Q,D}=Ŷ|Y_{A|Q}≠Ŷ) rises from 48.7% to 52.2%). This nuanced evaluation goes beyond aggregate metrics.

- **Parameter efficiency and long-context robustness**: EATQA trains only 4.5M parameters (0.06% of LLaMA-7B) via LoRA yet delivers consistent improvements. It handles longer documents effectively, with larger gains on longer-document groups (e.g., +3.5 F1 in the longest quartile, Table 5).

## Weaknesses

### Fatal

None. The core claims (SOTA results, contribution of each module, hallucination mitigation) are empirically supported.

### Major

1. **Architecture contradiction: "adapter tokens" vs. LoRA**: Section 4.2 (Model Architecture) describes "several trainable adapter tokens p = [p_1, ..., p_{N_p}] which are prepended to the key and value of each self-attention layer" — this is prefix-tuning. Section 5.2 (Implementation Details) states "we use LoRA ... which freezes the pretrained model weights and injects trainable rank decomposition matrices." These are two different parameter-efficient fine-tuning methods, and the paper never reconciles them. The parameter count (4.5M) is consistent with LoRA (e.g., rank 8 on Q,V projections for LLaMA-7B), suggesting LoRA was actually used and the "adapter tokens" description is incorrect. This must be resolved for the method to be reproducible. The paper should unambiguously state which adaptation method was used and correct the erroneous description.

2. **Missing operational details for the KL divergence term**: The distribution-bridging KL term KL(P(a,q) || q(a|e,q)) is motivated via an ELBO derivation (Eq. 2) and shown by ablation to be empirically valuable. However, the paper never explains *how* this KL divergence is computed during training. For autoregressive LLMs, the KL over entire output sequences requires an approximation (e.g., token-level KL under teacher forcing, or Monte Carlo sampling). The distribution P(a,q) is also not explicitly defined (the text implies it is the answer distribution without evidence, but this is never formalized). While a motivated practitioner could infer a reasonable implementation, the lack of operational detail undermines reproducibility for a component that is central to the method's claimed advantage. The derivation itself is a standard ELBO and not mathematically flawed; the issue is the missing implementation specification.

### Minor

1. **Slightly overstated "prior knowledge preservation" claim**: Table 4 shows that on already-known questions (where the model can answer correctly without the document), adding the document *reduces* accuracy from 88.8% to 85.8% for LLaMA2, and EATQA also shows 85.8% (the paper does not report the LLaMA2+document baseline for the same metric). The paper states "our model significantly mitigates the hallucination while keeping prior knowledge to solve the 'already-known' questions" (Section 6.2, p.7). A drop from 88.8 to 85.8 indicates some prior knowledge is lost. The overall picture remains positive — EATQA improves internal knowledge (34.8→37.1) and hallucination mitigation (48.7→52.2) — but the claim about "keeping prior knowledge" should acknowledge this trade-off rather than asserting it is fully preserved.

2. **EA→Q module mechanism not directly validated**: The paper shows (via ablation) that removing question restoration hurts QA performance, and the correlation analysis (Figure 3) shows a positive relationship between EA→Q and QE→A scores. However, the paper does not directly evaluate the quality of generated question restorations (e.g., via ROUGE/BLEU against the original question) or demonstrate that better restorations causally correlate with better answers at the instance level. The stated claim that EA→Q "enhances the casual relations between evidence and answers" is suggestive but not directly evidenced beyond the ablation. This does not weaken the paper's contribution (the empirical benefit is clear) but limits the mechanistic understanding.

3. **Conditional independence assumption not discussed**: The derivation assumes P_M(q|e,a,d) = P_M(q|e,a) (line 100), i.e., that once evidence and answer are given, the document provides no additional information for reconstructing the question. This is stated but never validated or discussed. If the evidence is incomplete, this assumption clearly breaks. The paper would benefit from a brief discussion of when this assumption is reasonable and how the method might degrade when it is violated.

### Trivial

- The paper uses "EA→Q" in the methodology text but "EAQ" in loss notation (L_EAQ) and figure labels. This minor inconsistency should be harmonized.

## Nice-to-Haves

- Report EATQA-13B results on QASPER for a direct size-matched comparison with RAG/CAD/RHO (currently Table 2 shows these baselines at 13B but EATQA only at 7B; the 7B results already outperform them, making this asymmetric comparison favorable to the baselines, but 13B results would strengthen the case).
- Report standard deviations or confidence intervals for QASPER results (Table 2), as the dataset is smaller (5,049 questions).
- Compare against a two-stage baseline (generate evidence then answer with the same model) in the main results table, rather than only in the ablation.

## Removed Points

These points from the reviewers were examined against the paper and removed or downgraded for the following reasons:

- **"KL derivation is unclear and potentially flawed"** — The derivation (Eq. 2) is a standard ELBO; the mathematical steps are correct. The real issue is the missing operational detail, which is retained as Major weakness #2 above. The "flawed derivation" framing was inaccurate and has been removed.
- **"The logical link between evidence extraction and the KL is never made clear"** — The paper explicitly states (after Eq. 2) that this KL minimizes the distribution distance between question answering with and without evidence, and is used as a regularizer for QE→A (line 168). The link is explained; the explanation could be clearer, but it exists. Removed as overclaimed.
- **Standard deviations for MultiRC results** — Table 1 reports significance testing (p < 0.001). This is standard for the field. Removed.
- **"The EA→Q benefit could be driven by sample difficulty"** — This is speculation without evidence. The correlation analysis grouped samples by difficulty to address precisely this concern. Removed.
- **Generic strengths from Strength Finder** — None were generic; all were specific and evidence-backed, so all retained.

## Novel Insights

The reviews surface that the paper's strongest empirical result (SOTA on MultiRC and QASPER) coexists with an unusually weak methodological exposition for a paper of this caliber. The architecture contradiction (prefix-tuning description vs. LoRA implementation) and the unspecified KL computation are not subtle issues — they are the kind of omission that a reader would catch on first pass. The reviews collectively identify a pattern: the paper is empirically well-executed but rushed in its write-up, with several sections that describe what the method does at the conceptual level without specifying how it is actually implemented. The most striking observation is that the two harshest criticisms (architecture contradiction and missing KL details) are not about the idea being wrong but about the paper being incomplete as a specification. This suggests the paper's acceptance hinges entirely on whether the authors can cleanly resolve these expositional gaps — the empirical contribution is not in dispute.

## Suggestions

1. **Resolve the architecture inconsistency immediately**: State unambiguously whether LoRA, prefix-tuning via adapter tokens, or a hybrid was used. If LoRA was used, correct the "adapter tokens prepended to key/value" description in Section 4.2. If a hybrid was used, describe it precisely. This is the single most actionable fix.
2. **Specify how the KL divergence is computed during training**: Define what P(a,q) and q(a|e,q) are as computational objects (e.g., output logit distributions at each token position under teacher forcing), and state whether the KL is summed or averaged over token positions, whether the stop-gradient is applied, etc. Even a single sentence specifying "token-level KL under teacher forcing" would resolve the ambiguity.
3. **Acknowledge the prior-knowledge trade-off in Table 4**: Add one sentence noting that on already-known questions, providing the document slightly reduces accuracy (88.8→85.8), which is expected since the document can introduce distracting information, and that the net benefit comes from improved handling of unknown questions.
4. **Evaluate question restoration quality directly**: Report ROUGE-L or BLEU between generated and original questions for the EA→Q module, and show that instances with better restorations also have better QA scores.

## Score and Decision

**Originality**: Good — the triplet generation framework is a novel way to unify evidence, answering, and question understanding within a single LLM, though each component individually is standard.

**Importance of research question**: High — hallucination in document-grounded QA is a central problem for deploying LLMs in knowledge-intensive settings.

**Claims support**: The core claims (SOTA results, module contributions) are well-supported. The "prior knowledge preservation" claim is slightly overstated.

**Soundness of experiments**: Good — thorough ablation, multiple backbone sizes, two datasets, statistical significance, and hallucination-specific analysis. The main gap is the missing KL implementation detail which affects reproducibility but not the validity of reported numbers.

**Clarity of writing**: Below average — the architecture contradiction and under-specified KL computation are significant clarity issues. The Bayesian derivation and its relationship to the training losses could be better organized.

**Value to community**: High — SOTA results on established benchmarks with a parameter-efficient method are practically useful.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>