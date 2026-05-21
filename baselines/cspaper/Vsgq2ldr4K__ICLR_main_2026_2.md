---
job_id: 35281a31-03e4-4e26-83fd-6e8205565a87
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Vsgq2ldr4K.pdf
paper: Reasoning with Sampling: Your Base Model Is Smarter Than You Think
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining probabilistic sampling, language-model reasoning, inference-time optimization, and RL-related analysis.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including Abstract, Introduction, Related Work, Method, Experiments, Results/Analysis, and Conclusion, and it presents a concrete algorithm with quantitative evaluation on multiple benchmarks.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious reviewer-targeted instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies whether reasoning gains typically attributed to RL post-training can instead be elicited from a base language model purely at inference time. The authors propose a training-free sampling method that approximately targets a sequence-level power distribution \(p^\alpha\) via an autoregressive Metropolis-Hastings procedure, and they evaluate it on MATH500, HumanEval, GPQA, and AlpacaEval 2.0 across three base models, comparing against base decoding, low-temperature sampling, and GRPO-trained models.

## Strengths
The paper asks a sharp and important question: how much of RL-posttraining’s apparent reasoning improvement is already latent in the base model and can be unlocked by better inference? That framing is timely and relevant, and it is broader than a narrow decoding tweak paper because it bears directly on how the community interprets RL gains.

The main technical idea is simple but meaningful. The distinction in Section 4.1 between low-temperature token-level sharpening and sequence-level power-distribution sharpening is clearly motivated, and **Proposition 1** gets at a real conceptual confusion that appears often in practice. The toy example around **Equations (7) and (8)** is helpful, because it makes concrete why “sum of exponents” and “exponent of sums” behave differently for future-path-sensitive reasoning.

The empirical results are surprisingly strong. **Table 1** shows that power sampling consistently improves over both the base model and low-temperature sampling, and is often competitive with or better than GRPO. The strongest evidence, in my view, is not just one win on one benchmark, but the pattern across tasks and model families. For example, on Qwen2.5-7B, the method improves HumanEval from 0.329 to 0.622 and AlpacaEval from 7.05 to 8.59, while also staying close to GRPO on MATH500. That is a meaningful result, especially because the method does not rely on additional training or a verifier.

I also appreciated that the paper does not only present headline numbers, but tries to characterize *why* the method behaves differently from RL. **Figure 4** is useful here: the histograms suggest that the proposed sampler moves generations toward higher-likelihood and higher-confidence regions under the base model, while preserving more spread than GRPO. That supports the authors’ central narrative better than raw benchmark numbers alone.

Similarly, **Figure 5** is one of the more convincing parts of the paper. It directly addresses a known issue with RL-style sharpening, namely diversity collapse. The figure shows that the proposed sampler gets strong pass@\(
k\) behavior without the same degradation observed for GRPO, which is a substantive point rather than cosmetic analysis. This makes the work relevant not only for pass@1 reasoning, but also for inference-time scaling and multi-sample usage.

Presentation is mostly clear. **Figure 1** does a good job summarizing the paper’s main empirical claim at a glance, namely parity with RL on in-domain math and stronger transfer on some out-of-domain tasks. **Figure 3** is also a helpful visual for the resampling-based Metropolis-Hastings procedure, especially for readers less familiar with MCMC over sequence spaces.

Finally, I think the paper’s scope is well judged. The authors do not oversell a full replacement for RL in all settings, and they include an unverifiable benchmark, AlpacaEval 2.0, which is important because one of the claimed advantages of the method is that it does not require a reward model or verifier.

## Weaknesses
1. **The paper’s compute story is underdeveloped, and this matters a lot for the practical significance of the method.**  
   The proposed sampler is explicitly an inference-time compute scaling method, and **Equation (12)** already indicates a quadratic-in-\(T\) token generation cost, approximately
   \[
   \mathbb{E}[\text{tokens}] \approx \frac{N_{\mathrm{MCMC}} T^2}{4B}.
   \]
   With the paper’s own settings, this is not a small constant-factor overhead. The appendix gives a rough estimate of about \(8.84\times\) standard inference cost for a MATH500-like output length, which is substantial. Yet the main paper does not provide a compute-normalized comparison against very natural baselines such as: best-of-\(n\) sampling from the base model under the same token budget, low-temperature best-of-\(n\), or simple reranking by base-model likelihood. Without such comparisons, it is hard to know whether the gain comes specifically from the MH targeting of \(p^\alpha\), or more generally from spending much more test-time compute. This is not a minor omission, because the paper’s central practical pitch is “training-free reasoning,” and inference cost is the obvious counterweight.

2. **There is an important algorithmic inconsistency in Algorithm 1 that needs correction.**  
   In Section 4.3, the text says that given a sample from \(\pi_k\), the goal is to obtain a sample from \(\pi_{k+1}\). However, in **Algorithm 1, line 7**, the acceptance ratio is written using
   \[
   \frac{\pi_k(\mathbf{x}')}{\pi_k(\mathbf{x})}
   \]
   rather than \(\pi_{k+1}\). If the chain at stage \(k+1\) truly targets the extended distribution over tokens \(x_{0:(k+1)B}\), then the MH acceptance ratio should be formed with that target, not the previous-stage one. As written, this is mathematically inconsistent with the stated objective of the stagewise transition. If this is only a typo, it is a serious one because it appears in the core algorithm. If it is intentional, then the method being implemented is not the one described. Either way, the paper needs to fix this and explain the exact target distribution at each stage.

3. **The paper blurs the distinction between exact and approximate sampling a bit too casually.**  
   The method is presented as an approximate sampler for the power distribution, which is fine. But several statements are stronger than the evidence supports. For example, **Algorithm 1** lists the output as
   \[
   (x_0,\dots,x_T)\sim p^\alpha,
   \]
   which is not literally true for finite \(N_{\mathrm{MCMC}}\), finite block size \(B\), and a staged construction over prefixes. Section 4.2 correctly recalls asymptotic MH convergence conditions, but Section 4.3 then introduces a heavily truncated and structured procedure with no argument that the finite-step chain is close to the intended target in any quantitative sense. This matters because the main empirical claims depend on the exact sampler not being necessary, but then the paper should be careful to present the method as a heuristic approximation rather than as if it samples from \(p^\alpha\) in a principled exact sense.

4. **The empirical evaluation is strong in benchmark count, but weaker than it should be in baseline design.**  
   The strongest missing baseline is a compute-matched inference-time baseline. Given **Table 1**, the paper concludes that “sampling directly from the base model can achieve results on par with GRPO,” but the more precise claim is that *this particular expensive structured sampler* can. Since the proposed method uses many repeated model calls and resampling steps, a fairer experimental question is whether it beats simpler uses of the same budget. For example, on HumanEval and MATH500, why not compare against multiple independent base-model samples with base-model likelihood reranking, or low-temperature samples under the same total token budget? This omission weakens the causal claim that the power-distribution target itself is doing the heavy lifting.

5. **The significance claim regarding RL should be framed more cautiously.**  
   The paper repeatedly leans on the idea that RL behaves mainly like distribution sharpening. The evidence provided is suggestive, especially **Figure 4**, where GRPO outputs concentrate in a high-likelihood, high-confidence region of the base model. But this is still indirect evidence. It does not rule out RL also changing the geometry of the response distribution in ways not captured by base-model likelihood histograms. In other words, the paper has persuasive evidence for a *sampling-based explanation of a large fraction of the observed gain*, but not decisive evidence that RL is merely sharpening. The distinction matters because the paper’s broader conceptual narrative is stronger than what is directly demonstrated.

6. **Some results in Table 1 are striking enough that they need more statistical context.**  
   **Table 1** contains several large swings, especially for Phi-3.5-mini-instruct on HumanEval, where GRPO drops to 0.134 while power sampling reaches 0.732. That is dramatic and potentially very interesting, but also exactly the kind of result that calls for confidence intervals, multiple seeds, or at least more discussion of variance and implementation details. For HumanEval in particular, minor formatting differences can strongly affect pass rates. The qualitative examples in **Table 2** and **Table 4** are suggestive, but they do not substitute for uncertainty estimates over the full benchmark.

7. **The exposition around the proposal distribution and reverse proposal terms is not fully explicit enough for reproducibility.**  
   In Section 4.2 and **Algorithm 1**, the paper says that the reverse transition probability is easy to calculate “by symmetry,” because one can treat \(\mathbf{x}^i\) as a resampled version of \(\mathbf{x}\). Conceptually this is fine, but the paper would benefit from explicitly writing the proposal density for a suffix-resampling move:
   \[
   q(\mathbf{x}'\mid \mathbf{x}) = \frac{1}{L} \, p_{\mathrm{prop}}(x'_{m:L}\mid x'_{<m}),
   \]
   with the understanding that \(x'_{<m}=x_{<m}\) and \(L=(k+1)B\) at the current stage. Then the reverse proposal has the analogous form. Right now the algorithm is understandable, but the exact transition probabilities are left a bit too implicit for a method whose correctness depends on them.

8. **The method is evaluated on only three relatively small open models, so the generality claims should be toned down.**  
   The paper does test across different families, which is good, but the models are all around the same rough small-to-mid scale. The title and some statements in the introduction suggest a broader conclusion, namely that “your base model is smarter than you think.” That may well be true, but the evidence here is for specific 7B-ish models and one mini model on a few benchmarks. This is enough for an interesting paper, but not enough to support expansive claims about base models in general.

9. **The qualitative evidence is mixed in its usefulness.**  
   **Table 2** and **Table 5** show examples where the method succeeds and GRPO fails, which is directionally helpful. However, **Table 3** is an example where both methods are correct, and it does not add much scientific value. I would have preferred more systematic qualitative breakdowns, for example categorizing when power sampling helps: arithmetic precision, code formatting, long-chain deductions, or answer extraction. That would connect the method more tightly to the “future-path planning” intuition introduced in Section 4.1.

10. **A few mathematical details are correct in spirit but presented a bit loosely.**  
   For instance, **Equation (4)** is written as the conditional under the power distribution, but the notation suppresses normalization over sequence lengths and the role of the support of completions. That is not fatal, but throughout Section 4, the paper moves quickly between “distribution over sequences of length \(T\)” and practical generation with EOS-based early stopping. Since the target distribution is sequence-level and the algorithm truncates at \(T_{\max}\), the paper should be more explicit about the exact state space being sampled, especially when claiming MH irreducibility and aperiodicity in Section 4.2.

## Questions
1. The most important clarification is about **Algorithm 1, line 7**. Should the MH ratio target \(\pi_{k+1}\) rather than \(\pi_k\)? If this is a typo, please state it clearly and confirm that the experiments used the correct acceptance ratio. If not, please explain why the previous-stage target is the right one.

2. Can the authors provide a **compute-matched comparison** against simpler inference-time baselines, such as best-of-\(n\) base sampling, best-of-\(n\) low-temperature sampling, or likelihood-reranked sampling, under approximately the same total token budget as power sampling? This would materially increase my confidence that the observed gains are specific to the proposed target distribution and not just a generic effect of more test-time compute.

3. How sensitive are the results in **Table 1** to random seed and implementation detail? In particular, the Phi-3.5 HumanEval numbers are unusually far apart. Even a brief report of variance across a few runs, or per-benchmark confidence intervals, would help.

4. Since the paper’s main conceptual claim leans on RL as sharpening, can the authors more carefully separate the empirical claim “power sampling recovers much of RL’s benefit” from the stronger interpretive claim “RL mostly sharpens the base distribution”? I would like to see a slightly more cautious discussion here.

5. Why was the proposal distribution fixed to low-temperature base-model sampling for most experiments? Did the authors try a higher-entropy proposal, a learned proposal, or a proposal equal to the base model itself? Some discussion of acceptance rate and mixing behavior as a function of \(p_{\mathrm{prop}}\) would be useful.

6. Can the authors report wall-clock latency or model-forward-pass counts in the main paper, not just token-count estimates? For a practical inference-time method, this is important.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper beyond standard considerations associated with evaluating LLMs on public benchmarks.

## Soundness Rating
3: good. The core idea is technically plausible and supported by meaningful experiments, but there is an important inconsistency in the algorithm statement, and the empirical support would be stronger with compute-matched baselines and uncertainty estimates.

## Presentation Rating
3: good. The paper is generally clear, well organized, and uses figures effectively, though some mathematical and algorithmic details need tightening.

## Contribution Rating
4: excellent. The paper makes a strong and interesting contribution by showing that a training-free sampler can recover a surprisingly large portion of RL-style reasoning gains, while also illuminating the role of sequence-level sharpening and diversity preservation.

## Overall Rating
8: Accept, good paper (poster). I have real concerns about the exact algorithm statement, compute accounting, and the lack of compute-matched baselines, so this is not at the “highlight” level for me. Still, the central result is strong, the idea is insightful, the experiments are compelling overall, and the paper is likely to influence how people think about RL versus inference-time reasoning.

## Reviewer Confidence
4: confident. I am comfortable with the MCMC and language-modeling aspects and checked the core equations and algorithm carefully, though a few implementation details would benefit from author clarification.