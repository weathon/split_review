- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 5, 8, 8
## Summary

InstructRAG proposes a framework where LMs generate explicit denoising rationales — explanations of how the ground-truth answer follows from retrieved documents — and then uses these rationales as ICL demonstrations or supervised fine-tuning data. The method requires no additional supervision beyond standard RAG and achieves consistent accuracy gains across five knowledge-intensive benchmarks (PopQA, TriviaQA, NQ, MultiHopQA, ASQA), with particularly strong noise robustness and task transferability results.

---

## Strengths

1. **Consistent and significant accuracy gains across five benchmarks.** Table 1 shows InstructRAG-ICL (Llama-3-70B) achieves the highest accuracy on all four short-form QA datasets (PopQA 65.5, TriviaQA 81.2, NQ 66.5, MultiHopQA 57.3), and InstructRAG-FT (Llama-3-8B) outperforms every trainable baseline (including Self-RAG and RetRobust re-implemented on Llama-3) across all datasets. The gains are substantial — e.g., NQ improves from 56.6 (vanilla SFT) to 65.7 (InstructRAG-FT), a 16% relative improvement.

2. **Robust denoising as retrieval noise increases.** Figure 3 shows that while baseline methods plateau or decline when the number of retrieved documents increases (lowering retrieval precision), InstructRAG-ICL and InstructRAG-FT continue to improve. This is the strongest direct evidence that the explicit denoising mechanism works as claimed.

3. **Self-synthesized rationales without external supervision.** The method generates rationales using the LM's instruction-following ability, with a 98% consistency ratio (substring match) on samples with at least one relevant document. This stands in contrast to Self-RAG (requires GPT-4 for reflection tokens) and RetRobust (requires GPT-3 for sub-queries), which rely on external model supervision.

4. **Strong out-of-domain task transfer.** Figure 4 shows that InstructRAG generalizes from PopQA to ASQA (short-to-long-form QA), from ASQA to PopQA, and from single-hop to multi-hop QA, consistently outperforming baselines in both in-domain and out-of-domain settings. Table 2(a) extends this to code generation (HumanEval), where InstructRAG-FT achieves 64.6 pass@1 vs. 59.8 for the base model with retrieval.

5. **LLM-as-a-judge evaluation confirms gains are not artifacts of pattern-matching.** Table 2(b) shows InstructRAG-ICL outperforms In-Context RALM under both pattern-based (62.1 vs. 56.8) and LLM-based (67.6 vs. 64.5) metrics, and InstructRAG-FT similarly beats vanilla SFT, verifying that improvements hold under semantic evaluation.

---

## Weaknesses

### Fatal
None.

### Major

1. **Rationale quality/faithfulness is not directly evaluated.** The paper claims that InstructRAG enables "easier verification of the predicted answers" and produces rationales for "better verifiability and trustworthiness," but the only sanity check on rationale quality is a substring match (does the rationale contain the ground-truth answer?), achieving 98% on samples with relevant documents but only 89% overall (line 492-493). The paper never directly evaluates whether the rationales correctly identify relevant vs. irrelevant documents, contain sound reasoning, or actually help a human verify the answer. The substring match is a necessary condition, not a sufficient one — a rationale could contain the answer while making incorrect claims about which documents support it. This gap does not invalidate the well-supported accuracy and robustness results (which stand on their own), but the specific claimed advantages in verifiability and trustworthiness are asserted without direct evidence.

2. **Missing chain-of-thought baseline.** The training-free comparisons include in-context RALM (direct answer prediction) and few-shot QA demonstrations, but not chain-of-thought prompting on retrieved documents (e.g., "think step by step" zero-shot or few-shot CoT). The template-based rationale ablation shows that heuristic-structured outputs underperform, but this does not address whether a simpler form of LM-generated intermediate reasoning (without the denoising instruction structure) would provide similar gains. Including a CoT baseline would help isolate whether the specific denoising structure drives the improvement or whether any extended intermediate reasoning suffices.

### Minor

3. **Rationales are post-hoc justifications, not traces of actual reasoning.** The rationale generation prompt (Table 1) includes the ground-truth answer and asks the LM to "explain how the contents lead to the answer." This produces synthetic training targets, not records of the model's actual reasoning process. The ablation study (Table 4) shows that removing the ground-truth answer during rationale generation causes only a 0.3–2.5% drop, suggesting that the model can often produce plausible rationales from parametric knowledge alone. The paper frames this positively (robustness), which is valid, but it also means the rationales' connection to the retrieved documents may be weaker than the "explicit denoising" framing suggests. The larger drops when removing retrieved documents (up to 5%) partially mitigate this concern.

### Trivial
None.

---

## Nice-to-Haves

- Adding a chain-of-thought baseline would strengthen the attribution of gains to the denoising structure vs. any intermediate reasoning.
- Including a brief discussion of the computational cost of generating rationales for the full training set would be helpful for practitioners.

---

## Removed Points

These points were raised in the input reviews but are removed after cross-checking against the paper:

1. **8.3% relative improvement computation is wrong** (Harsh Critic). ☞ **Removed.** Verified: comparing InstructRAG-FT vs. vanilla SFT per-dataset gives (8.52+6.22+16.08+1.96+8.68)/5 = 8.29%, confirming the claim is correct. The critic's attempted reconstruction was based on a different (unstated) comparison baseline.

2. **Rationales may be generated independently of the answer, undermining the denoising claim** (Harsh Critic). ☞ **Removed (re-framed to Minor point 3).** The paper transparently reports the ablation and frames it as robustness, a reasonable interpretation. The critic's stronger claim that this "undermines" the method is overstated — removing retrieved documents causes larger drops (up to 5%), confirming documents matter.

3. **Computational cost not discussed** (Harsh Critic). ☞ **Demoted to Nice-to-Have.** Standard data augmentation cost; not a substantive weakness.

4. **Paper does not discuss whether rationales reflect actual reasoning process** (Harsh Critic). ☞ **Incorporated into Minor point 3** at reduced severity. The paper explicitly describes these as "self-synthesized" rationales, not reasoning traces.

5. **Several generic strengths from Strength Finder** — e.g., "this paper addressed an important problem" framing removed. Only concrete, evidence-anchored strengths retained.

---

## Novel Insights

The most striking pattern across the reviews is that both the strengths and weaknesses center on the same feature: the rationales. The accuracy results are uniformly strong and uncontested — InstructRAG beats every baseline on almost every metric, often by wide margins. The critique targets the *interpretation* of *why* it works, not the *whether*. The missing CoT baseline and the unverified rationale quality are both questions about mechanism interpretation rather than empirical validity. This suggests the paper's core empirical contribution is solid, but its narrative framing (explicit denoising → verifiability) reaches slightly beyond what the evidence directly supports. The noise robustness experiments (Figure 3) provide the strongest mechanistic evidence but are somewhat under-emphasized relative to the "verifiability" framing.

---

## Suggestions

1. Add a direct evaluation of rationale faithfulness — e.g., have human annotators or an automatic method (NLI-based attribution) judge whether the rationales correctly identify relevant documents, ignore irrelevant ones, and support the answer. This would directly support the verifiability claim.

2. Include a CoT baseline (zero-shot or few-shot "think step by step" on retrieved documents) to clarify whether the denoising structure itself is responsible for the gains.

3. Consider tempering the "verifiability" and "trustworthiness" claims or explicitly noting that these properties are asserted but not yet directly evaluated, as the accuracy and robustness results are already strong enough to carry the paper.

---
