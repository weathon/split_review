Now I have a thorough understanding of the paper and can verify each claim. Let me produce the final consolidated review.

## Summary

This paper tackles the problem of adaptive adversarial attacks in vertical federated learning (VFL), where an adversary can corrupt a subset of client-server communication channels. The authors formulate finding the optimal set of clients to corrupt as an online optimization problem, decompose it into an inner adversarial example generation (AEG) problem and an outer corruption pattern selection (CPS) problem, and establish the equivalence of the CPS problem to a multi-armed bandit (MAB) problem. They propose the E-TS (Thompson sampling with Empirical maximum reward) algorithm, which uses the empirical maximum reward of each arm to construct a "competitive set" and restricts exploration to this set, reducing regret from $\mathcal{O}(\log T)$ per arm to $\mathcal{O}(1)$ for non-competitive arms. Experiments across six datasets spanning tabular, CV, multi-view, and NLP tasks show that E-TS converges faster and more stably than plain Thompson sampling and other baselines to the best attainable attack success rate.

## Strengths

1. **Novel problem formalization for adaptive client corruption in VFL.** The paper is the first to frame adversarial attack on VFL as an online optimization problem where the adversary adaptively selects which subset of clients to corrupt, going beyond fixed-corruption-pattern attacks (e.g., Pang et al. 2022, Qiu et al. 2022). The decomposition into an inner AEG problem and an outer CPS problem is clean and well-motivated (Sec. 3–4).

2. **E-TS algorithm with a principled exploration-reduction mechanism.** The core algorithmic idea — using the empirical maximum reward to define a competitive set and restrict TS exploration within it — is novel for MAB-based attack selection. The claimed regret bound of $D\,\mathcal{O}(\log T) + (N-D)\,\mathcal{O}(1)$ would strictly dominate plain TS when $D \ll N$, which is precisely the regime the combinatorial arm space creates. This is a non-trivial algorithmic advance.

3. **Consistent empirical superiority across diverse VFL tasks.** On all six datasets (tabular: Credit, Real-Sim; CV: FashionMNIST, CIFAR-10; multi-view: Caltech-7; NLP: IMDB), E-TS converges to the optimal ASR faster and more stably than plain TS, random corruption, and fixed-pattern baselines. The gap widens as the exploration space grows (e.g., from 120 to 3,276 arms in Fig. 3), demonstrating the algorithm's value exactly where it is needed most. Experiments are repeated for 10 trials with standard deviations reported.

4. **Realistic threat model and resource constraints.** The adversary is assumed to corrupt at most $C$ of $M$ clients under computational/bandwidth constraints, operates as a man-in-the-middle with no access to server parameters or other clients' embeddings, and uses only query-based feedback. This is grounded in prior security literature and more practical than assumptions of full model knowledge.

5. **Comprehensive ablation studies.** The paper systematically evaluates the effect of corruption constraint $C$, query budget $Q$, perturbation budget $\beta$, warm-up rounds $t_0$, and larger search spaces, providing practical guidance for algorithm deployment.

## Weaknesses

### Major
None.

### Minor

1. **The theoretical analysis is presented as a very brief sketch in the main paper.** The "Proof sketch" (Section 6) consists of three sentences, and Lemmas 1–2 and Theorem 1 are stated without any supporting argument. While full proofs presumably reside in the appendix (which was stripped by the parser), the main text's sketch is too sparse to validate the claimed $\mathcal{O}(1)$ bound for non-competitive arms or to assess how the analysis handles the concentration of the empirical maximum reward statistic. Readers cannot gauge the rigor of the theoretical contribution from the main paper alone.

2. **The NES noise sample size $n$ is not reported.** The paper describes NES gradient estimation using $n$ Gaussian noise samples (line 124) and notes that the number of perturbation updates per sample is $\lfloor Q/n \rfloor$ where $Q=2000$, but never specifies the value of $n$ used in the experiments. This parameter affects both query efficiency and gradient-estimation quality, and omitting it harms reproducibility.

3. **Defense evaluation is limited to one dataset.** The defense experiments (randomized smoothing, dropout, manifold projection) are conducted only on FashionMNIST. While these results are informative, including at least one additional dataset (e.g., CIFAR-10 or Credit) would strengthen the claim that the defense effects are not dataset-specific.

4. **No principled heuristic for setting $t_0$.** The ablation study (Fig. 2b) shows that $t_0$ is critical — too small risks excluding the optimal arm from the competitive set, too large diminishes E-TS's advantage — but $t_0$ is tuned per dataset (80 for vision, 50 for tabular, 40 for IMDB) without a principled selection criterion or adaptive termination heuristic. A practical adversary would need to know this in advance.

### Trivial

None.

## Nice-to-Haves

- An adaptive or data-driven criterion for terminating warm-up would strengthen the method's practical deployability.
- Reporting the NES parameter $n$ and the scaling parameter $\sigma$ would improve reproducibility.
- A brief complexity analysis of the per-round computational cost (NES optimization per sample × batch size × number of arms) would help practitioners understand deployment costs.

## Removed Points

These points were removed per the review guidelines; they are listed here for completeness but should be treated with caution:

- **Criticism about competitive arm definition being misaligned with MAB objective (Harsh Critic Point 1).** The critic argues that using maximum reward to define competitive arms conflicts with the mean-based regret objective. This is a misunderstanding: the competitive set is a conservative pre-filter that eliminates only arms that are *provably* suboptimal (their maximum reward never exceeds the optimal mean). Arms that survive are explored via standard TS, which operates on mean rewards. The definition is well-aligned as a pruning criterion. An arm with high variance that appears "competitive" under this definition is simply not pruned — TS handles it within the competitive set. The critic's claim that a low-variance arm close to optimal could be excluded is incorrect: over enough pulls, such an arm's maximum reward will exceed the optimal mean.

- **Criticism about the regret analysis being incomplete and the proof sketch not establishing the claimed bound (Harsh Critic Point 2, parts about missing proofs).** The paper states lemmas and a theorem with a "Proof sketch" label. Per the review guidelines, criticisms about missing appendix proofs are removed because the parser strips appendix content from all papers; full proofs exist in the original submission. The specific concerns about concentration of the empirical maximum reward and optimal arm exclusion cannot be verified or rebutted without the full proofs.

- **Criticism about not validating the inner AEG component against prior VFL AE methods (Harsh Critic Point 3).** The paper's contribution is the CPS algorithm (E-TS) for adaptive corruption pattern selection, not a novel AEG method. The experimental design correctly isolates the CPS contribution by using the same inner method (NES) across all baselines. Comparing NES against Pang et al. or Qiu et al. would address a different question and is outside the paper's scope.

- **Complaints about specific missing implementation details (complete training logs, hyperparameter disclosure beyond standard reporting).** These are nitpicks about reproducibility that are either addressed (most parameters are reported) or are not standard to include in a conference submission.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Expand the proof sketch in the main paper.** Even a one-paragraph sketch per lemma showing how the key challenges (concentration of the empirical maximum reward, warm-up phase, optimal arm exclusion) are handled would significantly improve the reader's ability to assess the theoretical contribution without consulting the appendix.

2. **Report the NES noise sample size $n$** and the scaling parameter $\sigma$ in the experimental setup, as these directly affect the query budget allocation and gradient estimation quality.

3. **Extend defense evaluation to at least one additional dataset** to rule out dataset-specific effects.

4. **Consider an adaptive warm-up termination criterion** based on the stability of the empirical competitive set, rather than a fixed $t_0$ per dataset.

## Score and Decision

**Originality:** The paper introduces a novel formulation for adaptive client corruption in VFL and a new MAB algorithm (E-TS) for exploration-space reduction. The problem framing is original and timely.

**Importance of research question:** Adversarial robustness in VFL is a practically relevant security problem. Adaptive attacks that go beyond fixed-pattern assumptions are an important direction.

**Claims supported:** The empirical claims are well-supported by experiments on six datasets with ablations. The theoretical claim is stated but presented as a brief sketch, making it hard to fully assess from the main paper alone.

**Soundness of experiments:** Experiments are well-designed with appropriate baselines, 10-trial repetitions, and standard deviations. The ablation studies are thorough.

**Clarity of writing:** The paper is well-structured and the problem formulation is clearly explained. The algorithm is presented with explicit pseudocode.

**Value to community:** The E-TS algorithm and the problem formulation open a new direction for adaptive attacks in VFL security. The empirical results provide a strong benchmark.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>