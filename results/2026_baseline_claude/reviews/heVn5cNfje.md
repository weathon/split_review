Now I have a complete picture of the paper. Let me write the review.

---

## Summary

The paper introduces **High-Entropy Sum (HES)**, a training-free data selection metric for LLM reasoning. Instead of averaging token entropy over an entire reasoning trace (which dilutes signal), HES sums the entropy of only the top 0.5% highest-entropy ("forking") tokens per sample. Higher HES indicates that a sample navigated more numerous or more uncertain decision points. The authors validate HES as a unified data selection criterion across Supervised Fine-Tuning (SFT), Rejection Sampling Fine-Tuning (RFT), and Reinforcement Learning (RL), demonstrating consistent improvements over random, length-, and difficulty-based baselines across math, code, and STEM domains.

---

## Strengths

- **Simple, broadly applicable metric with strong empirical validation.** HES requires only a single forward pass on the model being trained; it introduces no auxiliary reward model or annotation cost. Experiments span three training paradigms, four datasets, four base models (ranging from 0.6B to 8B parameters), and three domains (math, code, STEM). The core finding—that pruning the bottom 20% lowest-HES data from SFT consistently raises accuracy above the full-dataset baseline—is replicated across every domain and model combination tested (Tables 1–4).

- **The cross-model proxy-scoring finding is practically valuable.** The experiment showing that HES scores computed by a 0.6B model are nearly as informative for training an 8B model as scores from the 8B model itself (32.12% vs. 31.14% avg. in Table 1) is a notable and actionable result. If HES captures dataset-intrinsic complexity rather than model-specific uncertainty, it implies one cheap scoring pass suffices for large-scale dataset curation.

- **Thorough ablation design.** The paper compares HES against a comprehensive set of competing signals (average entropy of all tokens, average entropy of high-entropy tokens only, total entropy sum, length, difficulty, and absolute-threshold HES), making it possible to isolate exactly why the relative-percentile, sum-based formulation outperforms alternatives. The sensitivity analysis across high-entropy token ratios (0.005 to 1.0) and data selection ratios (0.1 to 1.0) is presented across three domains (Figures 3–4), showing that the 0.5% setting is both near-optimal and robust over a wide hyperparameter range.

- **The asymmetric RL sampling insight is novel and theoretically well-motivated.** The finding that selecting the highest-HES *positive* rollouts while keeping *random* negative rollouts (Pos-High, Neg-Rand) outperforms both the full-batch baseline and strategies that also curate the negative pool (Table 6) provides a principled and non-obvious conclusion: quality-focused curation of positive examples is beneficial, but artificially constraining negative diversity is harmful.

---

## Weaknesses

### Fatal
None.

### Major

1. **The Figure 1 motivation is in tension with the downstream selection logic, and the paper does not resolve this tension explicitly.** Figure 1 shows that *incorrect* responses have substantially higher HES (normalized mean 0.68) than *correct* responses (0.29). The paper uses this large gap to argue that HES is discriminative. However, the training-data-selection strategy then selects the *highest*-HES samples as the most valuable for learning. Without explicit explanation, this implies the paper is preferentially selecting the samples that most resemble "incorrect" generation behavior. The paper never directly addresses this apparent paradox. The underlying logic—that in guaranteed-correct SFT data, high HES signals maximally complex reasoning paths rather than errors—is coherent, but it is never stated explicitly. Readers following the motivation from Section 2 will reasonably conclude that high HES is a quality *problem*, not an asset, and may distrust the selection direction. This needs to be surfaced clearly, because the insight is actually sound and interesting.

2. **No statistical significance testing anywhere in the paper.** Several key comparisons involve small absolute differences. In RFT (Table 5, per-query k=2), the improvement from Random (30.37) to Highest-HES (31.38) is 1.01 points; at k=8 it is 0.97 points. In RL (Table 6), the improvement over Full-Batch (20.63) from the best strategy (21.30) is 0.67 points. Given that these are averaged over 16 samples per benchmark and over 7–8 benchmarks, it is unclear whether these differences exceed random variation. The absence of confidence intervals, standard deviations, or even repeated runs makes it impossible to assess whether the RL result—the paper's most novel training application—is a reliable finding or noise.

3. **Confounded comparison in the RL experiments.** The RL baseline "Full-Batch" uses all 32 rollouts per query; all down-sampling strategies use 16. "Pos-High, Neg-Rand" thus uses fewer positive *and* fewer negative examples per update than Full-Batch, changing both the positive/negative ratio and the total batch size simultaneously. Any advantage could arise from the changed ratio (more negative relative to positive) rather than HES quality per se. A controlled ablation—e.g., "Pos-All, Neg-Rand-Half" or varying the positive/negative ratio independently of HES—is needed to isolate the HES contribution from the composition change.

### Minor

1. **The HES-in-RL performance gain over Full-Batch is small, and the paper's framing ("significantly surpassing") overreaches the data.** A 0.67-point average improvement from 20.63% to 21.30% does not warrant the phrase "significantly surpassing" without statistical support. The wording should be calibrated to the evidence.

2. **The 0.5% threshold's physical interpretation is underdeveloped.** For a sequence of length N=2000 (typical in these datasets), 0.5% corresponds to 10 tokens. Whether this constitutes the "critical forking points" in a principled sense is not discussed. In very short sequences this might degenerate; in extremely long chain-of-thought sequences (e.g., 32K tokens), 0.5% means 160 tokens, which may over-represent transitional passages rather than just decision points.

3. **RFT per-query vs. global-pool asymmetry is not fully explained.** The paper notes that per-query selection outperforms global pool selection and hypothesizes this is due to query diversity. However, it does not control for total dataset size or investigate whether adding a diversity constraint to global-pool HES selection would recover the gap.

### Trivial
None worth noting.

---

## Nice-to-Haves

- A qualitative analysis of which tokens actually receive the highest entropy in correct vs. incorrect reasoning traces (e.g., are they operator choices, number substitutions, or logical pivots?) would strengthen the mechanistic story.
- Reporting compute costs (GPU hours) for HES scoring vs. training-a-reward-model vs. LLM-based selection would make the efficiency advantage concrete.

---

## Novel Insights

The most genuinely novel insight, which the paper establishes but underemphasizes, is the *asymmetry in how HES should be applied to positive vs. negative examples in RL*. While it is intuitive to select "hard" positive examples, the finding that curating negative examples toward low-HES *hurts* performance—whereas keeping a diverse random negative pool is beneficial—suggests that RL for reasoning requires qualitatively different coverage objectives for positive and negative sides of the value function. This principle (maximize positive quality, maximize negative diversity) is not derivable from GRPO theory alone and is a meaningful empirical contribution. A second novel insight is the cross-model consistency of HES: because top-0.5% entropy tokens correspond to dataset-intrinsic lexical and structural branch points (choices between formulae, problem-solving strategies, etc.), a tiny model's HES scores generalize to large model training—implying that HES measures the data's complexity, not the scoring model's capacity.

---

## Suggestions

- Directly state in Section 3.1 or 4.1 why selecting *high*-HES data improves training even though Figure 1 shows incorrect responses have higher HES. The bridging argument ("in SFT, correctness is already guaranteed; high HES among correct samples means more complex but tractable reasoning paths") is sound and should be made explicit.
- Add repeated-run error bars or at minimum report standard deviation across the 16 evaluation samples per benchmark to support the RL claim.
- Add an RL ablation fixing the positive/negative ratio while varying whether positives are HES-selected vs. random, to cleanly isolate the HES contribution from the batch composition change.
- Provide a brief cost analysis (FLOPs or wall-clock time) for HES scoring relative to training, particularly for the 3.2M-sample Open-Math-Reasoning dataset.

---

## Score and Decision

The paper addresses a practical and well-defined problem—efficient data curation for LLM reasoning training—with a simple, well-validated metric. The comprehensive multi-paradigm, multi-domain, multi-model experimental sweep is among the strongest aspects of the submission. The main structural weakness is the unresolved tension between the Figure 1 motivation and the selection direction, and the lack of statistical rigor for the RL result. These are significant presentation and methodology gaps, but they do not invalidate the core empirical findings, which are consistent and replicated. Overall, this is a solid, practically useful contribution above the median ICLR submission.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>