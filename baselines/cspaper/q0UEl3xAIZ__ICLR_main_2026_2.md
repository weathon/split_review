---
job_id: f983ff9e-bd90-4b52-86ea-d0a49f73bdbb
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: q0UEl3xAIZ.pdf
paper: Goal-Oriented State Reduction of Unknown Game Dynamics to Produce Effective Strategies
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, probabilistic/Bayesian inference, state abstraction, and interpretability in a game environment.

## Minimum Quality
Pass ✅. The paper contains the core ingredients of a research submission, including abstract, introduction with related-work context, methods, quantitative experiments, results analysis, and discussion; while there are notable weaknesses in novelty, evaluation breadth, and mathematical clarity, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious text, or other attempts to manipulate automated reviewing in the provided paper content.

# Expected Review Outcome:
## Summary
This paper studies Goal-Oriented Environment Inference (GOEI), a previously proposed model-based reinforcement learning method for reducing large observation spaces into a smaller set of latent “core” states that are sufficient for outcome prediction. The authors evaluate GOEI on a simplified two-player, five-card version of Hol’s der Geier, and report that it reaches near-Nash-equilibrium performance against an NE opponent while reducing the observation space from 15,542 possible observations to 452 representative states. The paper also compares GOEI to tabular Q-learning and analyzes what information is retained in the learned reduced states using mutual information.

## Strengths
The paper has a clear and concrete empirical objective: to test whether the previously proposed GOEI framework transfers from an abstract environment to a more game-like setting with combinatorial observations. That makes the contribution easy to understand, even if it is more of a validation/application paper than a new algorithmic one.

The experimental setup is at least internally coherent for the stated question of environment inference under fixed opponent behavior. The separation between environment inference and strategy testing, described in Section 3.3, is logically aligned with the authors’ narrower claim that they are evaluating the quality of the inferred model rather than full online adaptation.

There is one genuinely interesting empirical observation in **Table 1** and **Figure 2**: the best GOEI configuration achieves median reward rates very close to 0 against the NE opponent, while using a dramatically smaller state representation than the raw observation space. In particular, the best row in **Table 1** \((\beta,\alpha)=(0.2,25)\) reports median reward \(-0.010\), with \(|S_2^*|=8\), \(|S_3^*|=31\), and \(|S_4^*|=408\), compared with observation counts \(300, 4209, 11028\). This is a substantial compression result within the confines of the chosen task.

**Figure 2A** is also useful rather than decorative. It shows that GOEI improves faster than the tabular Q-learning baseline in the authors’ protocol, and the comparison to the dashed \(\pi_0\) baseline gives a readable anchor for the scale of gains. **Figure 2B** complements this by showing that the learned state count grows over training and stabilizes far below \(|O_t|\), which supports the paper’s central message that the method is performing selective abstraction rather than simply memorizing all observations.

The mutual-information analysis in **Figure 3** is a reasonable first attempt to probe what the learned abstraction retains. Even though the interpretation remains limited, it is still better than reporting compression alone with no attempt to analyze the semantics of the learned state space.

Presentation is uneven, but the high-level story is easy to follow. The game description in **Figure 1** is helpful for grounding the environment, and the paper is generally readable without requiring the reader to reconstruct the experimental protocol from scratch.

## Weaknesses
1. **The paper’s contribution is quite limited relative to ICLR standards, because the main technical method is not new and the empirical validation is narrow.**  
The core algorithm, GOEI, is explicitly introduced as prior work from Takahashi et al. (2024), and this submission mainly applies it to a single small game domain. The paper does not present a new inference objective, a new theorem, a new planning algorithm, or a broader benchmark suite. As written, this is closer to a case study showing that an existing method works on one toy-to-small-scale environment than a substantial advance in representation learning or RL. That matters because ICLR main track typically expects either stronger methodological novelty or broader, more convincing empirical scope.

2. **The environment is extremely small and simplified, which undercuts the strength of the scalability and realism claims.**  
The title and abstract use language suggesting reduction of “unknown game dynamics” in a realistic setting, but the actual environment is a two-player, five-card version of Hol’s der Geier, not the standard larger version. The authors themselves acknowledge this limitation on **Page 8-9**, stating that they adopted the five-card version due to memory limitations. This is not a minor caveat. In a five-card game with only four decision rounds effectively modeled, it is much easier for compact abstractions to appear effective than in the standard setting or in larger imperfect-information games. So the central claim of practical usefulness in “more realistic” settings feels overstated relative to the evidence.

3. **The empirical comparison is too weak to support strong claims about GOEI’s effectiveness as an RL method.**  
The only direct learning baseline is tabular Q-learning in **Table 1** and **Figure 2A**. That is a very weak comparator for a model-based latent-state method operating in a partially observed combinatorial game. There is no comparison to stronger model-based approaches, belief-state approaches, planning with learned latent models, or even simple abstraction baselines. There is also no comparison to a tabular model-based learner without state reduction, which would be the most direct way to isolate the benefit of GOEI’s abstraction rather than the benefit of having any model at all. Because of this, the main empirical conclusion is narrower than the paper suggests: GOEI beats tabular Q-learning in this setup, but the paper does not show that GOEI is competitive with reasonable alternatives for rich-observation game settings.

4. **The evaluation protocol is somewhat favorable and does not test the central practical setting emphasized in the introduction, namely online adaptation to opponents.**  
In Section 3.3, the authors deliberately separate environment inference from strategy optimization, train only on fixed-strategy games (Rand vs. NE), then evaluate the strategy induced by the inferred model against NE. This is acceptable for a controlled study, but it substantially weakens the practical message in the introduction about online learning and adapting to opponents. The model is trained on trajectories generated by fixed policies, including the NE policy used at test time. Even if the held-out evaluation episodes are separate, this is still a relatively benign offline-like setting. The authors acknowledge this limitation in the discussion, but the consequence is important: the paper does not demonstrate that GOEI is effective in the interactive nonstationary setting that is advertised as motivation.

5. **The hyperparameter selection and reporting are not fully convincing, and the evaluation averages are unusual.**  
The paper searches over several \((\beta,\alpha)\) settings for GOEI and several learning rates for Q-learning, then reports the best settings in **Table 1** and **Figure 2A**. However, it is not clearly explained whether hyperparameters were chosen using a validation protocol independent of the final reported metric. The wording on **Page 6** suggests that the “average reward rate across 3,000 epochs was used to evaluate the performance on each training set,” which sounds close to selecting based on the same statistic later emphasized in the paper. This is not catastrophic leakage, but it is not a strong evaluation practice either. Also, averaging reward over all epochs from 1 to 3000 mixes early and late performance in a way that can obscure actual asymptotic quality.

6. **The mathematical exposition around the inference model is underspecified and at points inconsistent enough to make it hard to verify the method from the main paper alone.**  
A few concrete examples:
   - In **Equation (4)**, the reduced-state requirement is expressed as equality of reward distributions for all future action sequences \(\mathcal{A}_{t:4}\). This is a strong condition, but the paper does not discuss identifiability or whether the variational objective actually targets this condition in any principled sense, beyond citing prior work.
   - In **Equation (5)**, the factorization of \(P(r,\mathcal{A},\mathcal{S},\Theta \mid \mathcal{O})\) is unusual and omits several terms one would expect if this were a full generative model over all rounds. The indexing is also odd: the product is over \(t=2\) to \(3\), yet the text later discusses \(\Theta_t^A\) and \(\Theta_t^S\) across multiple rounds, and the final sentence of the paragraph says “finally find \(\Theta_2^A\), and \(s_1\),” even though \(s_1=o_1\) was previously fixed. This makes the dependency structure hard to reconstruct.
   - In **Equation (7)**, the factorization of \(q(\Theta)\) is written as \(\prod q^R_{s,a}(\Theta^R_{s,a})\, q_{t,o}(\Theta^S_{t,o})\, q_{t,s,s'}(\Theta^A_{t,s,s'})\), but the index ranges of the product are missing, so the expression is not mathematically complete as written.
   - In **Equation (8)**, the notation \(q^{(i)}_{t,o}(\Theta^S_{t,o})=\mathrm{DP}(\Theta^S_{t,o}\mid \alpha,a^{(i)}_{t,o})\) is nonstandard and vague. A Dirichlet process is a distribution over measures, not a simple categorical vector in the same way as a Dirichlet distribution. The paper’s prose explanation on **Page 5** reads more like a Chinese Restaurant Process intuition, but the actual variational form and truncation/representation are not specified in the main text.
These issues matter because the submission leans heavily on a probabilistic inference formulation, yet the reader cannot cleanly verify what is actually optimized from the main paper.

7. **The paper does not sufficiently justify the claim that the learned state representation is interpretable or explanatory.**  
This is a major theme in the introduction and abstract, but the actual interpretability evidence is weak. **Figure 3** shows per-feature mutual information between the learned state and observable features, but this does not explain the latent states in a way a human can use. In fact, the authors admit in Section 5 that they “could not give a verbal explanation of the reduced state representation more concretely than Figure 3.” I appreciate the honesty, but then the paper should tone down the explainability framing. Compression is not the same thing as explanation, and the current evidence mainly supports compactness, not interpretability.

8. **The paper’s treatment of Nash equilibrium as a target is somewhat ambiguous, and the “nearly optimal” claim should be phrased more carefully.**  
The main reported median reward against NE is around \(-0.010\) for the best GOEI setting in **Table 1**, which is indeed close to zero, but not identical. Given 10,000 test games per epoch and 21 seeds, even small deviations could be statistically meaningful; no confidence interval or significance test is provided for the final comparison to zero or to Q-learning. Moreover, “nearly optimal” here means “nearly unexploitable against one specific NE opponent in this simplified game,” not globally optimal play or convergence to an NE policy. The phrasing in the abstract and results section blurs that distinction.

9. **Some of the empirical analyses are suggestive but not as informative as they could be.**  
For example, **Figure 4** shows sensitivity to \(\alpha\) and \(\beta\), but the interpretation is speculative and not tightly connected to measurable quantities such as posterior concentration, state growth rates, or stability of assignments. Similarly, the state-count comparison to “NE states” in **Figure 2B** and **Table 1** is intriguing, but the construction of NE state counts on **Page 5-6** is described only briefly and is not transparent enough to serve as a strong interpretive baseline.

10. **There are presentation and notation issues that, while not fatal alone, accumulate.**  
There are multiple grammatical problems and several awkward sentences, for example on **Page 4-5** (“This approach is ensurred by Bayes theory,” “approximated with approximated probability distribution,” “GOEI could earned rewards”). More importantly, notation is sometimes inconsistent, such as switching between \(P\) and \(p\), and referring to \(q(\theta)\) in prose after defining \(q(\Theta)\). These issues reduce confidence that the mathematical details have been communicated carefully.

11. **The literature positioning is thinner than it should be for this problem setting.**  
The paper cites the authors’ prior GOEI paper and some general RL/XAI references, but it does not adequately situate itself with respect to broader model-based RL and state-abstraction work for rich-observation or partially observable games. Given that the paper’s main claim is about compact latent state representations for planning in a game with many observations, a stronger comparison to adjacent lines of work would help the reader understand what GOEI is buying beyond this one case study.

## Questions
1. The biggest issue for me is evaluation scope. Could the authors clarify whether they can provide results on a larger version of Hol’s der Geier, even if only partial, or on at least one additional environment? A second environment would materially increase my confidence that the reported compression-performance tradeoff is not highly game-specific.

2. Please clarify the hyperparameter-selection protocol. Were \((\alpha,\beta)\) and the Q-learning learning rate chosen using a separate validation criterion, or were they selected based on the same test-style reward summaries reported in **Table 1**? A precise description here would help assess the strength of the empirical claims.

3. Please make the probabilistic model in **Equations (5)-(8)** more explicit. In particular:
   - What exactly is the variational family for the DP-based clustering variables?
   - What are the full index ranges in **Equation (7)**?
   - Is there a truncation level or finite approximation to the DP in implementation?
   - What is the exact ELBO being optimized?
A more explicit derivation would substantially improve confidence in the method.

4. The paper motivates explainability, but the current evidence is limited to mutual information in **Figure 3**. Can the authors provide a more concrete interpretation of representative states, for example by listing the most probable observations assigned to several high-mass states or by showing how state identity changes recommended actions? That would make the interpretability claim much more credible.

5. Can the authors quantify uncertainty around the “near-NE” claim? For example, confidence intervals over the final reward rates, or significance tests comparing GOEI to zero reward and to the best Q-learning baseline. Right now **Table 1** suggests the effect is real, but formal uncertainty would help.

6. Since the introduction emphasizes online adaptation, do the authors have any preliminary evidence for joint environment inference plus strategy improvement, rather than the separated training/testing protocol of Section 3.3? Even a small-scale experiment would help bridge the gap between motivation and evaluation.

7. Please clarify the construction of the “effective state number of NE” reported in **Table 1** and plotted in **Figure 2B**. This comparison is potentially interesting, but the current description is too terse for me to verify whether the baseline is fair and interpretable.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
2: fair. The core empirical result is plausible and the experiments are not obviously invalid, but the mathematical specification is underspecified in the main paper, the baselines are weak, and the evaluation protocol only partially supports the broader claims.

## Presentation Rating
2: fair. The high-level narrative is understandable and the figures are helpful, but notation, grammatical quality, and explanation of the probabilistic model need substantial improvement.

## Contribution Rating
1: poor. The paper primarily validates an existing method on one small simplified game, with limited novelty and limited evidence for broader impact beyond that case study.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
There is a real empirical signal here, especially the compression result in **Table 1** and the learning behavior in **Figure 2**, but the submission falls short on contribution strength, breadth of evaluation, and mathematical clarity. With a stronger experimental scope, clearer probabilistic specification, and a more modest framing around interpretability and realism, this could become a stronger paper.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and familiar with the surrounding RL/state-abstraction area, though some implementation details of the variational DP inference are too underspecified in the main paper to verify completely.