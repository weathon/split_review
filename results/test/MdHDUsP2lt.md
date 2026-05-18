Now I have thoroughly verified the paper's content. Let me produce the final consolidated review.

---

## Summary

This paper proposes Denoised Predictive Imagination (DPI), an information-theoretic auxiliary objective for model-based RL that simultaneously minimizes mutual information with past observations/latents and maximizes predictive information about future observations/latents. The objective is derived as a single Lagrangian (Eq. 3) that unifies four mutual-information terms, which are bounded using CLUB, NCE, and variational decoders, then added as an auxiliary loss to Soft Actor-Critic. Experiments on six DeepMind Control Suite tasks with natural video backgrounds show DPI outperforms baselines on three dense-reward tasks and produces reconstructions that blur background noise while preserving the agent.

## Strengths

1. **Principled information-theoretic framework unifying multiple learning signals.** The paper derives a single Lagrangian (Eq. 3) that simultaneously minimizes past information (observation→latent and latent→latent) while maximizing future predictive information. The four resulting loss terms (\(I_{\mathrm{LTC}}, I_{\mathrm{CLUB}}, I_{\mathrm{Rec}}, I_{\mathrm{NCE}}\)) are shown to be upper/lower bounds on specific MI terms, providing a unified theoretical motivation that prior work's objectives (predictive coding, contrastive learning, reconstruction) emerge naturally from a single formulation (Sections 4.1–4.3).

2. **Strong empirical performance on realistic, high-distraction environments.** Under natural video backgrounds from Kinetics 400 (RGB, random categories, unseen test videos), DPI achieves higher rewards than all eight baselines on Cheetah Run, Walker Walk, and Cartpole Swingup (Figure 4). In the maximally stochastic random background setting (unique image per frame), DPI consistently achieves higher mean reward with narrower confidence intervals than all baselines (Figure 5).

3. **Demonstrated denoised reconstructions.** Figure 1 shows that DPI reconstructs only the task-relevant agent while blurring the background, confirming that the learned representation successfully compresses away temporally correlated noise. This provides direct visual evidence that the information-theoretic objective achieves its intended effect.

4. **Comprehensive and rigorous evaluation.** The paper compares against eight state-of-the-art methods (Dreamer, Dreamer-V2, TIA, Denoised MDPs, DBC, SPR, VSG, TPC) across six DMC tasks and three distinct environment types (standard, natural background, random background), using optimal hyperparameters from each respective paper.

## Weaknesses

### Fatal

None.

### Major

1. **Empirical claims in the introduction and conclusion are overstated relative to the evidence.** The introduction states DPI "outperforms eight existing state-of-the-art models on six modified DeepMind control (DMC) tasks," and the conclusion states DPI "consistently either surpassed or equaled the best of eight baselines in performance." These statements do not match the results in Figure 4. Under natural backgrounds, DPI clearly leads in only 3/6 tasks (Cheetah Run, Walker Walk, Cartpole Swingup). In Reacher Easy it is competitive but not clearly ahead of all baselines. In Pendulum Swingup and Cup Catch (sparse-reward tasks), DPI underperforms relative to several baselines. While Section 5.4 honestly acknowledges "Failure under Sparse rewards," the headline claims in the abstract, intro, and conclusion create an expectation of broad dominance that the data do not support. This mismatch between claims and evidence weakens the paper's credibility.

### Minor

2. **Baseline tuning asymmetry for noisy environments.** The paper uses baseline hyperparameters from their original publications — which were tuned on standard, noise-free settings or simpler grayscale distractors — without adapting them for the modified RGB video background environments. Since DPI is explicitly designed for noisy observations while baselines are used out-of-the-box, the comparison may overstate DPI's relative advantage. The paper acknowledges that "the main reasons for the degraded performance of most baseline methods was changing the background image to RGB" (Section 5.4), but does not investigate whether noise-adapted baselines would narrow the gap. This is a common limitation in the distractor-RL literature but should be acknowledged more explicitly.

3. **Theoretical derivations presented too compactly for the claimed rigor.** The derivation connecting the intuitive Predictive Information / Information Bottleneck motivation to the practical loss function (Eqs. 6–13) involves several inequality steps and variational approximations presented very concisely. While each inequality is verifiably correct after careful inspection — for instance, the bound in Eq. 6 follows from conditioning reducing entropy (\(H(z_{1:t}|a_{1:t-1}) \leq H(z_{1:t})\)), and the lower bound in Eq. 10 follows from the reverse chain rule with fewer conditioning variables — the paper does not spell out these justifications. The repeated deferrals to the Supplementary Material (e.g., "Due to space limitations, all subsequent derivations and details are in the Supplementary Material") mean the main text's theoretical narrative reads more as a sketch than a complete derivation.

4. **Limited statistical evidence.** Results are reported with 95% confidence intervals from only three runs per task. Several confidence intervals overlap (e.g., Reacher Easy in Figure 4), making it difficult to assess whether DPI's advantages are statistically meaningful. A supplementary table of final mean/variance would aid interpretation.

### Trivial

5. **Inconsistency in claims across sections.** The abstract says DPI "surpasses four state-of-the-art approaches across six distinct scenarios" while the introduction says it "outperforms eight existing state-of-the-art models." These are contradictory (four vs. eight) and neither matches the nuanced results. This should be harmonized.

## Nice-to-Haves

- A table reporting final mean reward and standard error across seeds for each task/environment would be more informative than learning curves alone.
- An ablation isolating the contribution of each of the four loss terms (\(I_{\mathrm{LTC}}, I_{\mathrm{CLUB}}, I_{\mathrm{Rec}}, I_{\mathrm{NCE}}\)) on a single task would clarify which components drive performance. (Mentioned but not shown in the main text — likely in the supplementary.)
- Computational cost comparison (parameters, training time per step) relative to baselines would help assess the practical cost of the additional auxiliary losses.
- Tuning baselines' learning rates or architectural components for the noise setting (or running DPI in the original grayscale setting and comparing to published numbers) would strengthen the empirical claims.

## Removed Points

- **"The theoretical derivation of the core objectives is not sound"** (from Harsh Critic). Removed because this is factually incorrect. I verified each inequality against the paper's text. (i) Eq. 6: \(I(z_{1:t}) \leq E[\log p(z_{1:t}|a_{1:t-1})/\prod p(z_k)]\) follows directly from \(H(z|a) \leq H(z)\) (conditioning reduces entropy). (ii) The factorization in Eq. 7 using the history model is a standard chain-rule expansion. (iii) Eq. 10's lower bound is valid because conditioning on fewer variables (\(z_{k+1},a_k\) vs. \(z_{k+1:T}\)) gives higher entropy, making the sum a valid lower bound. (iv) The claim that the "second term \(I(z_k;a_k|z_{k+1})\) is simply left out" is incorrect — the score function \(\sigma(z_k,a_k,z_{k+1})\) in Eq. 12 includes actions, bounding the full \(I(z_{k+1},a_k;z_k)\), not just \(I(z_k;z_{k+1})\). The paper also discusses the decomposition explicitly (lines 140–141). The derivations are sound; the presentation is compact but not flawed.

- **"The connection between PI intuition and actual losses is asserted rather than argued"** (from Harsh Critic). Removed because this is a presentational preference, not a substantive weakness. The paper traces a clear path: PI is defined as \(I(x_{\text{past}};x_{\text{future}})\), the IB principle is introduced for compression, a two-level Lagrangian is constructed (Eqs. 1–3) operating on both observation→latent and latent→latent MI, and each term is then bounded. The logic is coherent even if compact.

- **"I_LTC is described as an upper bound but the final expression is reminiscent of a variational bound on a different quantity"** (from Harsh Critic). Removed because the paper explicitly states (lines 118–130) that Eq. 8 (the full bound) and Eq. 9 (the variational approximation) are an upper bound on \(I(o_{1:t};z_{1:t})\). The derivation is consistent.

- **"Three runs with 95% CI is a weak sample size"** downgraded to trivial and subsumed under Minor Weakness 4.

- **Formatting/style nitpicks, missing section content, and complaints about parser-stripped appendix content** removed per hard rules.

## Novel Insights

None beyond the paper's own contributions. The observation that the harsh critic's primary complaint (the theoretical derivation) is factually incorrect upon verification while the actual weakness (overstated claims) is a presentational issue rather than a scientific one is noteworthy: it shows the paper's core technical contribution is sound, and the main problem is how the results are communicated, not what was done.

## Suggestions

1. Revise the introduction and conclusion to state precisely: "DPI achieves higher rewards than all baselines on Cheetah Run, Walker Walk, and Cartpole Swingup under natural video backgrounds, and is competitive in Reacher Easy; it underperforms on sparse-reward tasks where all methods struggle." This honest characterization would make the positive results more credible.
2. Either tune the learning rates of baselines for the noise setting (holding their architecture fixed) or run DPI in the standard grayscale setting against published results to demonstrate that DPI's advantage is not purely due to environment-specific tuning.
3. Add a table of final mean rewards with standard errors to complement the learning curves.
4. Include the ablation study in the main paper, not just the supplementary.

## Score and Decision

This paper presents a novel and principled information-theoretic framework for learning denoised representations in model-based RL. The theoretical derivation is sound (the harsh critic's primary objection is factually incorrect upon verification), and the empirical results on dense-reward tasks with realistic video backgrounds are promising. However, the empirical claims in the abstract, introduction, and conclusion are overstated relative to what the data show — the paper claims broad superiority but the evidence only supports it on 3 of 6 tasks under natural backgrounds. The baseline comparison also has a tuning asymmetry that is not adequately acknowledged. These are addressable issues: the theory is solid, the method is interesting, and the results on dense-reward tasks are genuinely strong. The paper would benefit from honest recalibration of its claims and improved evaluation practices.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>