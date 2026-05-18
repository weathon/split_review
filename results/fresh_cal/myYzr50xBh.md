Now I have all the information I need. Let me construct the final review.

## Summary

This paper identifies that only 0.1% of LLM parameters — selected by the top entries of the gradient squared (sensitive parameters derived from the empirical Fisher information) — suffice for zeroth-order fine-tuning, and that this mask can be derived from pre-training data (C4) and transferred as a static sparsity pattern across diverse downstream tasks. The authors combine this with 4-bit quantization (SqueezeLLM) into SensZOQ, achieving sub-8GiB ZO fine-tuning of 7B-scale LLMs that outperforms full ZO fine-tuning, ICL, LoRA, and Prefix Tuning on the same quantized base model.

## Strengths

1. **Identifies and validates extreme static sparsity (0.1%) for ZO fine-tuning that transfers from pre-training data.** Figure 3 shows C4-gradient-derived masks cover >20× more task-gradient entries than weight-magnitude baselines, and Figure 5b confirms the performance gap between C4-derived and task-specific static masks is small at 0.1% sparsity. This is the paper's core novel finding.

2. **SensZOQ enables ZO fine-tuning of Llama2-7B under 8 GiB memory while outperforming full ZO fine-tuning and in-context learning.** Table 1a shows SensZOQ achieves 77.8 average accuracy vs. ZO Full FT 68.3 and ICL 68.9 on Llama2-7B, with consistent trends across Mistral-7B and OPT-6.7B (Tables 1b–1c). The memory footprint is validated in Figure 1.

3. **Outperforms ZO parameter-efficient fine-tuning baselines (LoRA, Prefix Tuning) on the same 4-bit quantized base model.** Table 1a shows SensZOQ (77.8) outperforms LoRA (74.0) and Prefix Tuning (72.8) on Llama2-7B, with the pattern holding across all three model families.

4. **Extensive ablation validates sensitive parameters against five alternative sparsity strategies.** Figure 5a shows that only the sensitive-parameter mask maintains near-flat performance from 10% sparsity down to 0.1%, whereas largest-weight, smallest-weight, random, and GraSP masks all degrade sharply below 1% sparsity.

5. **Evaluation across three 7B-scale LLMs (Llama2-7B, Mistral-7B, OPT-6.7B) and nine diverse datasets.** The experimental design covers sentiment (SST-2), inference (RTE, CB, BoolQ), coreference (WSC), word sense (WiC), commonsense (COPA, WinoGrande), and language modeling (Wiki2), supporting the generality claim.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Overclaimed scope regarding on-device/mobile deployment.** The paper motivates SensZOQ by citing "mobile phones and laptops" (abstract, introduction) and "on-device personalization" throughout, but all experiments benchmark CUDA memory on GPU devices. While demonstrating sub-8 GiB GPU memory is impressive and relevant for laptops with discrete GPUs, no experiment runs on actual mobile hardware, measures inference/fine-tuning time on such hardware, or addresses CPU/accelerator compatibility. This gap between framing and evidence does not undermine the technical contribution (memory-efficient ZO fine-tuning is clearly demonstrated), but the claims about mobile-phone deployment should be tempered.

2. **Unsubstantiated claim about "pioneering step" on math tasks.** The paper states "To the best of our knowledge, there are no ZO-LLM research yet evaluated on harder commonsense reasoning or math tasks. We take a pioneering step in this direction" (line 125–126). However, the evaluated tasks include only harder commonsense reasoning (COPA, WinoGrande) and no math datasets (e.g., GSM8K, MATH). The claim about math tasks is unsupported by the experiments and should be removed or the experiments should include math benchmarks.

3. **Mask selection procedure is underspecified.** The paper states that sensitive parameters are derived from "a small batch of C4 texts" (line 129), but does not specify the batch size, number of examples, total compute time, or whether computing the gradient for mask selection requires backpropagation (which the method otherwise avoids during fine-tuning). Since the mask is a critical component of the method, these details matter for reproducibility and for evaluating the one-time cost of the approach.

4. **Baseline training details for LoRA and Prefix Tuning are underspecified.** The paper reports that LoRA and Prefix Tuning are applied "on top of the same quantized LLM weights as SensZOQ" (line 194) but does not clarify whether these baselines are fine-tuned with first-order or zeroth-order methods, nor what optimizer (SGD vs. Adam) or hyperparameters are used. This affects the fairness of the memory comparison (FO training requires caching gradients/activations) and the reproducibility of the results.

### Trivial

1. **The "random seed trick" from MeZO is mentioned but not explained** (line 56). While this is standard in the ZO literature, a brief clarification would help self-contained reading.

## Nice-to-Haves

- Report memory benchmarks for all baselines in Table 1 (not just SensZOQ) to directly validate the memory-efficiency claim against LoRA, Prefix Tuning, and ZO Full FT under identical settings.
- Include sparsity ablation below 0.1% (e.g., 0.01%) to determine whether 0.1% is a genuine threshold or a convenient choice.
- Add a statistical significance discussion for close comparisons (e.g., SST-2: SensZOQ 84.1 vs. ZO Full FT 83.9).

## Removed Points

These points were identified by the reviewers but are removed or demoted for the reasons stated:

- **"Theoretical foundation under-validated in main text (Theorem 1 missing)."** The theorem statement and proof are in the appendix, which is standard practice. The extracted text shows the section explicitly setting up this connection ("The theoretical support of sensitive parameters can be derived from the lens of SPSA gradient estimator and Fisher information matrix as follows:"). This is a parser artifact, not an author omission.
- **"Comparison with SparseMeZO not apples-to-apples."** The paper explicitly frames this as a comparison in the *static* sparsity regime (line 262: "static sparsity regime") and labels the baseline as "weights with smallest magnitude (SparseMeZO's sparsity patterns)." The paper acknowledges the distinction. This concern would only apply if the paper claimed to beat dynamic SparseMeZO, which it does not.
- **"Missing figure descriptions" and "figures absent from extracted text."** These are parser/extraction artifacts, not flaws in the paper.
- **"Statistical significance not discussed."** The paper reports mean and std over 3 trials, which is the standard for this line of work. Requesting formal significance tests for every comparison is a nice-to-have, not a weakness.
- **"Strengthening the Paper" suggestions** (explore sparsity below 0.1%, quantify mask selection cost, add memory benchmarks) are legitimate suggestions but are better placed as Nice-to-Haves, not weaknesses, since they do not undermine the existing claims.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Narrow the deployment claims to scope consistent with the evidence (laptops with discrete GPUs; replace or qualify "mobile phones").
2. Remove or substantiate the "pioneering step on math tasks" claim — either add math benchmarks or delete the reference to math.
3. Specify how the C4 gradient for mask selection is computed (batch size, number of examples, whether backprop is used) and note that this is a one-time pre-computation cost.
4. Clarify whether LoRA and Prefix Tuning baselines use FO or ZO optimization, and if FO, acknowledge the memory overhead difference.

## Score and Decision

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>