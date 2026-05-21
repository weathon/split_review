---
job_id: 995a4ca2-335e-4f51-8ba5-5ec2df21d028
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: nnwvwge40d.pdf
paper: Reinforcing General Reasoning Without Verifiers
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on reinforcement learning for LLM reasoning, likelihood-based optimization, and general ML methodology for language models.

## Minimum Quality
Pass ✅. The paper contains the required scientific components, including abstract, introduction, methodology, experiments with quantitative results, and conclusion/discussion material. While I have several substantive concerns about assumptions, comparisons, and claim calibration, I did not find a fatal theoretical error, test leakage, or a completeness issue that would justify desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not detect hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies how to extend R1-Zero-style reinforcement learning to general reasoning domains where answer verification is difficult or unavailable. The core proposal, VeriFree, replaces explicit verifier rewards with the model probability of the reference answer conditioned on a sampled reasoning trace, yielding an objective that the paper shows is equivalent in expectation to verifier-based RL under a single-correct-answer assumption, with a lower-variance gradient estimator. Empirically, the paper evaluates VeriFree on Qwen3 base models across MMLU-Pro, SuperGPQA, GPQA-Diamond, and several math benchmarks, and reports performance comparable to or better than a model-based verifier baseline, alongside ablations on RLOO, tokenization-aware splitting, and answer-equivalence handling.

## Strengths
1. The paper tackles a real bottleneck in current RL-for-reasoning pipelines, namely the dependence on explicit verifiers. That problem formulation is important and timely. A verifier-free route that still stays close to the RLVR perspective is more interesting than yet another reward-model variant.

2. The derivation in **Section 2.2**, especially **Equation (4)** and **Equation (5)**, is clean and conceptually useful. Under the stated exact-match, single-answer assumption, the transformation from the verifier objective to the probability-of-reference-answer objective is straightforward and mathematically coherent. The decomposition into a reasoning term and a reference-answer term is also intuitive and helps explain why the method is not just plain supervised fine-tuning on answers.

3. The variance-reduction argument is one of the more convincing parts of the paper. The intuition around Rao-Blackwellization is sound, and **Theorem 1 / Equation (6)** matches that intuition: analytically marginalizing over the answer token sequence instead of sampling it should reduce Monte Carlo variance. I also appreciate that the paper does not oversell this as a magic theorem, it is a sensible estimator argument tied directly to the proposed construction.

4. The empirical section is fairly extensive for a main-track paper. The results span multiple model sizes and several general reasoning benchmarks. In particular, **Table 1** and **Table 2** show a consistent pattern that VeriFree is competitive with, and often slightly stronger than, the verifier-based baseline on MMLU-Pro and SuperGPQA. For example, on **Table 1**, Qwen3-8B-Base-VeriFree reaches 67.2 average on MMLU-Pro versus 65.9 for Qwen3-8B-Base-Verifier, and on **Table 2** the same pair gives 38.0 versus 37.1 on SuperGPQA. This cross-scale consistency matters more than isolated wins.

5. I found **Figure 2** and **Figure 3** helpful. **Figure 2** does a good job of visually separating the standard RLVR pipeline from the proposed "sample reasoning trace, patch reference answer, score via conditional probability" workflow. **Figure 3** is simple, but as a reviewer I appreciated that it makes the implementation-level distinction concrete rather than hiding behind equations.

6. The paper includes practical details that often get skipped in papers of this flavor. The tokenization-aware handling of the patch point in **Section 2.4** is one of those annoyingly important engineering details that can absolutely make or break the method in practice. The ablation in **Figure 6 (Left)** gives this point some empirical backing instead of leaving it as a hand-wavy implementation note.

7. The training-efficiency comparison in **Figure 4 (Left)** is useful. Even if the final gains are not huge, the curve suggests that VeriFree learns at least as efficiently as the verifier baseline and often better. That is aligned with the lower-variance story and makes the method practically attractive.

8. The paper is stronger than average in showing that the method is not narrowly confined to general-domain multiple-choice benchmarks. The transfer experiment in **Figure 5** is a nice touch: training on non-math data and still getting gains on math benchmarks supports the claim that the method is affecting reasoning behavior more broadly, not merely memorizing answer patterns in one domain.

## Weaknesses
1. The central equivalence claim is only exact under a very restrictive assumption that does not match the motivating application. The paper is explicit in **Section 2.2** that the derivation from verifier-based RL to VeriFree requires a unique correct answer string with exact matching, replacing semantic equivalence $\mathbbm{1}_{\{y \equiv y^\star\}}$ by $\mathbbm{1}_{\{y = y^\star\}}$. But the entire motivation of the paper is general reasoning, where semantic equivalence and multiple valid surface forms are precisely the difficult part. So there is a mismatch between the nice theory and the actual target regime. The paper partially acknowledges this, but then leans quite hard on empirical success to bridge the gap. That is acceptable as an empirical paper, but the presentation should be more restrained: the method is theoretically exact for the easiest case and heuristically extended to the case that actually matters.

2. Related to the above, the main paper does not fully resolve whether VeriFree is robust when the reference answer is only one of many valid realizations. The ablation on equivalence classes in **Section 3.3** and **Figure 6 (Right)** is directionally useful, but it is limited to math and framed as a small add-on experiment. For a paper whose headline claim is “general reasoning without verifiers,” this issue should be much more central. If multiple phrasings are common, optimizing $\pi_\theta(y^\star \mid x, z)$ may unintentionally penalize semantically correct but differently worded answers. That matters scientifically because it changes the object being optimized from correctness to conformity with one reference string.

3. The baseline comparison is not as clean as it first appears. In **Section 3.1**, the verifier baseline uses the setup from Ma et al. with reward components beyond correctness, including a format penalty and a length penalty. VeriFree, by contrast, uses a different reward construction entirely and no verifier. This makes the comparison somewhat muddy because the baseline is not a pure “same objective, different estimator” comparison. If the paper wants to claim that VeriFree is better because of variance reduction and not because of differing reward shaping, then the baselines should be aligned more tightly. As written, a skeptical reader could argue that part of the gap is due to different inductive biases in the reward design rather than the absence of a verifier per se.

4. The paper repeatedly attributes the empirical advantage to lower variance, but the evidence for that mechanism is indirect. **Theorem 1** proves lower variance for the single-sample estimator under the exact-match setting, which is fine. But the empirical support in the main paper is basically the learning curves in **Figure 4 (Left)** and the claim that this is due to reduced variance. That is plausible, not demonstrated. There is no direct measurement of gradient variance, reward variance, or estimator SNR across training. This matters because the paper’s narrative is not merely “our method works,” it is “our method works for this principled reason.” Right now the principle is partly proven in a simplified setting and then inferred, perhaps too confidently, as the driver of the practical gains.

5. Some of the more ambitious interpretive claims are overstated relative to the evidence. The statement in **Section 3.2** that model confidence $\pi_\theta(y^\star \mid x, z)$ is “a good reasoning capability proxy” is too broad given the evidence shown in **Figure 4 (Right)**. What the figure really shows is a correlation during one training trajectory on Qwen3-8B base, on one benchmark, with confidence evaluated on the reference answer. That is a much narrower claim. A strong correlation along training does not imply this quantity is a reliable proxy for reasoning quality across models, tasks, or datasets. It may also partly reflect increased answer-format conformity or overfitting to benchmark style.

6. The evaluation focuses mostly on multiple-choice and short-answer settings, and the training data is explicitly filtered to keep answers under seven tokens in **Section 3.1**. This is a practical choice, but it narrows the scope of the conclusions. The paper sells itself as extending R1-style training to “general reasoning,” yet the main-paper evidence is concentrated on tasks where reference answers are short and evaluation is still fairly structured. The longer-answer experiment exists only later in the supplementary material. Based on the main paper alone, I am not convinced the method is ready for open-ended reasoning tasks where the answer space is much less canonical.

7. There is a mathematical presentation issue in the way the practical estimator is introduced. In **Equation (7)**, the notation makes $R_i = \pi_\theta(y^\star \mid x, z_i)$ and $A_i$ a leave-one-out centered version of the same quantity, but the paper glosses over an important dependency question: are gradients through $R_i$ and $A_i$ stopped inside the policy-gradient-style reasoning term, or are they differentiated as part of the full objective? From **Equation (5)** it looks like the second term carries the direct derivative of $\pi_\theta(y^\star \mid x,z)$, while the first term should treat the scalar reward as a weight in REINFORCE style. But the practical estimator in **Equation (7)** could be misread as backpropagating through everything. The intended gradient flow is inferable, but it should be stated explicitly because this is exactly the kind of ambiguity that causes implementation mismatch.

8. The comparison to JEPO and LaTRO is conceptually useful in **Section 2.3**, but the empirical evidence is oddly pushed out of the main paper despite being highly relevant to the paper’s novelty claim. If the authors want to argue that their probability-weighted answer term is the key distinction, that should really be demonstrated in the main experimental section. Otherwise the section risks reading as “we are different and probably better,” with the concrete supporting evidence deferred elsewhere.

9. **Figure 1** is visually compelling but also slightly too promotional relative to the nuance in the tables. For example, on some settings the gains over the verifier baseline are modest, and on some tasks in **Table 3** the verifier baseline is stronger. The figure supports the high-level story that VeriFree is competitive, but the text around it sometimes drifts toward “surpasses” language more often than the data fully warrants. The paper would benefit from being a bit less chest-thumping and a bit more precise about where the method wins, where it ties, and where verifier-based training remains stronger.

10. The practical scope of the claimed compute advantage is not quantified carefully enough in the main paper. The introduction emphasizes reduced compute and memory because no verifier model is needed, which is reasonable. But the training loop still requires extra forward passes for patched reference answers, and the actual wall-clock, throughput, or memory savings are not tabulated in the main paper. Since efficiency is a major selling point, this should be measured directly rather than asserted qualitatively.

## Questions
1. The most important clarification would be around the multi-answer setting. Can the authors quantify, on a benchmark where multiple correct surface forms are common, how often VeriFree assigns low reward to semantically correct but non-reference answers? Even a small controlled study would help distinguish “the single-reference approximation is harmless” from “it works only because the datasets are highly canonicalized.”

2. Please clarify the exact gradient flow for **Equation (7)**. In implementation, is $R_i = \pi_\theta(y^\star \mid x, z_i)$ detached when used in the reasoning-term coefficient $A_i \cdot \nabla_\theta \log \pi_\theta(z_i \mid x)$, with only the second term carrying the direct derivative through $\log \pi_\theta(y^\star \mid x, z_i)$? Writing this explicitly would substantially improve reproducibility and avoid confusion about whether the estimator matches **Equation (5)**.

3. Can the authors provide a cleaner verifier baseline that uses matched reward shaping, or alternatively an ablation of the current baseline with and without the extra format and length terms described in **Section 3.1**? This would make it easier to attribute gains specifically to the proposed objective and estimator.

4. The paper attributes faster learning in **Figure 4 (Left)** to lower variance. Do the authors have direct empirical measurements of estimator variance, reward variance, or gradient norm variance for VeriFree versus the verifier baseline? Even one controlled plot would materially strengthen the mechanistic story.

5. The tokenization-aware split in **Section 2.4** is interesting and **Figure 6 (Left)** suggests it matters. Could the authors report how often the naive text split actually causes token mismatch in practice, and whether the failure mode is systematic across tokenizers or mostly specific to the chosen template and model family?

6. The confidence-analysis claim in **Figure 4 (Right)** should probably be narrowed. Can the authors test whether average $\pi_\theta(y^\star \mid x, z)$ correlates with generalization across checkpoints on more than one benchmark or model size? That would make the “reasoning capability proxy” statement much more convincing.

7. Since the main paper trains on short answers only, can the authors summarize in the rebuttal how performance changes as reference-answer length increases? I would especially like to know whether there is a degradation regime where the patched-answer likelihood becomes less useful as a reward.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are evident from the main paper. The work trains and evaluates LLMs on standard reasoning datasets and does not introduce a new dataset involving sensitive personal data or human subjects. Standard caveats about misuse of stronger reasoning models apply, but nothing in the paper rises to the level of requiring formal ethics review.

## Soundness Rating
3: good. The method is technically plausible, the core derivation is sound under its assumptions, and the experiments are reasonably broad. My hesitation is that some claims are stronger than the direct evidence, especially beyond the single-answer exact-match setting.

## Presentation Rating
3: good. The paper is generally clear, the figures are useful, and the method is understandable. However, a few mathematical and empirical claims would benefit from tighter wording, and some crucial comparison details are deferred or under-explained.

## Contribution Rating
3: good. The paper makes a meaningful contribution by reframing verifier-based RL as a verifier-free probability objective and by showing competitive performance on general reasoning benchmarks. I do not view it as a complete resolution of reasoning without verifiers, but it is definitely a worthwhile step for the community.

## Overall Rating
8: Accept, good paper (poster). The paper has real substance: a crisp and useful reformulation, a sensible lower-variance argument, and convincing empirical evidence that the method is competitive in practice. I still have meaningful concerns about assumption mismatch, claim calibration, and the cleanliness of baseline comparisons, so this is not in highlight territory for me, but it is comfortably above threshold.

## Reviewer Confidence
4: confident. I am comfortable assessing the RL/objective-design aspects and checked the main derivations and empirical tables carefully. A few implementation details remain somewhat implicit, but I am unlikely to have misunderstood the central contribution.