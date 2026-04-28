# Sufficient and Necessary Explanations (and What Lies in Between)

- Decision: Reject
- Scores: 5, 6, 3, 5, 5

## Abstract
As complex machine learning models continue to find applications in high-stakes decision making scenarios, it is crucial that we can explain and understand their predictions. Post-hoc explanation methods provide useful insights by identifying important features in an input $x$ with respect to the model output $f(\x)$. In this work we formalize and study two precise notions of feature importance for general machine learning models: \emph{sufficiency} and \emph{necessity}. We demonstrate how these two types of explanations, albeit intuitive and simple, can fall short in providing a complete picture of which features a model finds important. To this end, we propose a unified notion of importance that circumvents these limitations by exploring a continuum along a necessity-sufficiency axis. Our unified notion, we show, has strong ties to other popular definitions of feature importance, like those based on conditional independence and game-theoretic quantities like Shapley values. Crucially, we demonstrate how a unified perspective allows us to detect important features that could be missed by either of the previous approaches alone.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
To address vague notions of feature importance in many XAI methods, the paper introduces formal definitions for sufficiency and necessity for local feature-based explanations. The authors further present a unified notion of sufficiency and necessity through a joint convex optimization problem to generate explanations that are both sufficient and necessary. The empirical results show that while existing feature importance methods can identify sufficient features, they fall short in finding necessary features.

### Strengths
The paper is mostly easy to read, every definition and theorem/results are relevant to the discussion and do not feel like the authors have included them for the sake of including math and notation. I also appreciate the authors for recognizing the need for auxiliary user studies in their limitations to highlight the fact that theoretical desiderata does not necessarily translate to real world impact/performance.

### Weaknesses
Having said that, the paper could improve on a couple of things:
1. Natural language explanation of "sufficiency" and "necessity" in Section 2 (I know this is in the introduction). Since they are the central concepts of the paper, it would be beneficial to really drive home what these mean in plain English for the reader.
2. The experiments section (detailed below)

The experiment setup was difficult to follow, a lot of missing details that I had to assume. For example, I couldn't find what the $L^0$ metric is defined (I am assuming that is the cardinality of the resulting $S$ for each method at thresholds). Similarly, the role of the threshold $t$ was unclear. I am assuming features with attribution/importance higher than $t$ will be included in $S$, but the paper does not explicitly mention that. It might be worth answering what the effect of adjusting $t$ is. 

Moreover, motivation for the tabular dataset experiment is very weak. What is the significance of investigating stability (and a synthetic dataset)? I know in the introduction, the authors ask the question "when do necessary and sufficient sets differ"? Perhaps this is something that the authors should mention in this section too. Note that this is not the case for the image classification experiment, which explicitly outlines its purpose (line 346).

Most importantly, I, as a reader, am unsure of the main takeaway from the experiments apart from the technical contributions of the paper at work. For example, what should we make of the result that necessary explanations are sufficient? This is an important question to answer since the abstract mentions that the paper demonstrates how strictly sufficient and/or necessary explanations fall short in providing a complete picture.

### Questions
Questions:
- Line 89: Is $f(\mathbf{x}_{S}, \mathbf{X}_S)$  a typo? I'd imagine one of them should be from the complement?
- Theorem 4.1 shows existence of $S^{*}$, do you have any theoretical results on uniqueness? Or can there be a unique solution in the first place?
- What happens when $\rho(f(\mathbf{x}) - f_{\emptyset}(\mathbf{x})) < \varepsilon$? (i.e. prediction is close to baseline)

Notes:
- I would suggest following a more standard notation for set complements: $S^\complement$, though I know having a superscript in a subscript may not be ideal
- Figure references in Section 6.2.2 "Sufficiency vs. Necessity" paragraph may be incorrect?
- Line 414: "demonstrateLemma"
- Line 424: $g_{\theta}: \mathcal{X} \to \mathcal{X}$ is a really big typo. Only found out when I looked at A.2.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a novel approach to sufficient and necessary subset explanations, proposing a method to identify subsets along a (symmetric) spectrum of necessity and sufficiency. The authors present theoretical results illustrating the properties of this unified approach and its connections to established importance measures, such as conditional independence and Shapley values. They demonstrate the effectiveness of their approach through experiments on both tabular and image data.

### Strengths
- **Clarity and Novelty**: The paper is well-written and extends existing work with a creative new approach to subset explanations.
- **Theoretical Contributions**: The authors provide a thorough theoretical analysis of their method, detailing its properties and connections to existing notions of feature importance.
- **Empirical Evaluation**: The framework’s applicability is demonstrated through diverse experiments, supporting the practical relevance of the proposed subset explanations.

### Weaknesses
1. It would be helpful if the main paper, prior to the experiments, provided a more detailed overview of how solutions are computed.

2. In the experiments section, you mention using a relaxed optimization approach for image data. Does this imply that, for tabular data, the exact solution is found by examining all subsets? Additionally, is there any investigation into the guarantees or potential limitations of the relaxed approach compared to the original problem?

3. In the abstract (Line 15), "feature importance" is used to describe sufficient and necessary sets. However, "feature importance" may not be the most precise term for these concepts.

4. The implications of Theorem 5.1 require further elaboration. Comparing different subsets feels akin to comparing different players in different games or players competing in their own games. If I understand correctly, searching within P_{uni} involves finding the feature subset with the highest Shapley Value in its own game, evaluated against its complementary subset. This paragraph could benefit from further clarification to ensure readers fully grasp its significance.

### Questions
1. Why did you choose to use marginal distributions in defining sufficiency (L89)? Most literature on sufficient explanations relies on conditional distributions, and even in some experiments, you use conditional distributions.

2.  What advantage does controlling minimality with a parameter like \( \tau \) provide, rather than defining minimal sufficiency directly? Calibrating \( \tau \) could be complex, especially as the existence of solutions for specific \( \tau \) values is uncertain. If this choice were removed, how would it impact your approach?

3. Given the focus on local prediction, why not define necessity as an average out of a subset that diverges significantly from the current prediction of the considered observation (e.g., \(1 - \epsilon\)), instead of using the average prediction? This definition might align more closely with interpreting necessity as the minimal feature set required to maintain the current prediction of the considered observation.

4. In all your results, would it not be necessary first to assume the existence of a solution to the problem given \( \tau \)?

5. Your unifying solution is defined as a combination of sufficient and necessary subsets using weights \( \alpha \) and \( 1 - \alpha \). Why not allow for any convex combination where \( \alpha_1 + \alpha_2 = 1, alpha_1, alpha_2 in (0, 1) \)? Would that significantly impact your results?

### Missing Citation

In your related work on sufficiency, you may want to reference [1], a follow-up to Wang et al. (2021) published at NeurIPS 2022, which proposes a more tractable approach for tree-based models:

> [1]: "Consistent Sufficient Explanations and Minimal Local Rules for Explaining Any Classifier or Regressor," Salim I. Amoukou, Nicolas J.B Brunel, NeurIPS 2022.

I am willing to increase if my questions and weakness comments are addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors consider the problem of feature importance, i.e., quantifying the influence of different input features in the context of supervised learning, which has become quite popular in explainable AI in the recent past. They propose new measures of sufficiency and necessity of feature subsets, as well as a convex combination between the two. They also consider the optimisation problem of finding (small) sufficient/necessary feature subsets.

### Strengths
Interesting and up-to-date topic, well-written paper, thorough experimental study.

### Weaknesses
The first problem I have with this paper is that I find the definition of necessity flawed, or at least not very meaningful. The definition of sufficiency says that a feature subset S is sufficient if the function f projected to S remains eps-close to the original function using all features, which does make sense. Naturally, then, I would have expected that a subset S is called necessary if its complement is not sufficient. At least, this is the common duality between necessity and sufficiency/possibility also found in other branches of the literature (e.g., in modal/possibilistic logic).

Instead, the authors call a subset S necessary if f projected to the complement of S remains close to the default (average) prediction with no features. First, as already said, this does not establish a "duality", but apart from that, this definition is very questionable by itself. It somehow suggests that staying close to the default prediction is something bad, while moving away from it is good. Besides, it also leads to formal problems. For example, suppose that f is indeed a (close to) constant function. Then, according to the definition, all feature subsets are necessary, which is counter-intuitive. 

The pathology outlined in the beginning of Section 4 is also a consequence of the flawed definition, I would say. Here, a feature subset is sufficient, but at the same time, its complement "contains important features". Again, this is completely counter-intuitive. How can a subset be sufficient if it misses important features?

Why is super-sufficiency an interesting property? Isn't it expected that adding more features will keep sufficiency? More interesting would be minimality: S is minimally sufficient if no feature can be removed from S without losing sufficiency. Analogously for super-necessity.

The "unification" is merely a convex combination of the two measures of sufficiency and necessity. Such convex combinations are routinely used in (multi-objective) optimisation, but why should we call them unification? Sure, one obtains both measures as special cases, for alpha=0 and alpha=1, respectively, but then it's more a generalisation than a unification.

The two perspectives in Section 5 are strange and in a sense again somewhat misleading. First, the notion of conditional independence is not defined in the standard way. Normally, conditional independence is a relation on random variables (used in probabilistic graphical models, for example). But why should we speak of conditional independence in the case of (5)?

The connection to the Shapley value is flawed as well. Normally, each feature is treated as a player and assigned a Shapley value. In Theorem 5.1, however, an entire feature subset S is treated as a single player, and its complement as a second player. Why should one consider such a partition as a game, and what does it help? A different game is then needed for every player. How do we connect this to the standard Shapley value? Eventually, with only two player S and S_c, the entire game is specified by the four values v(\emptyset),  v(S), v(S_c), v([d]). These are also the values/approximations looked at in the definition of sufficiency/necessity, so it's not very surprising to find a relationship here.

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes to merge _sufficency_ and _necessity_ notions into one unified optimization problem $P_{\text{uni}}$ and solving this combined optimization problem. Therein, the paper is interesting and shows that this unified approach retrieves explanations unlike baseline methods.

### Strengths
- **Good Contribution**: While I think the contribution can be strengthened (see weaknesses), the presented approach is very interesting. Joining and optimizing both conditions leads to very interesting explanations, which seem to be not retrievable by other methods. The work is sound and carried out well.

- **Theoretical Connections to Game Theory**: The paper connects the novel optimization problem $P_{\text{uni}}$ with well-established concepts like the Shapley value. While I think the discussion and interpretation is under-developed (see weaknesses) this connection can have impact on the line of research regarding Shapely values and hierarchical explanations.

- **Synthetic Experiments**: I like that the paper studies the approach in synthetic environments! This is often not done anymore and can be very insightful of what the method is actually doing. The paper studies the stability of the method in this setting, which is good but leaves more to be desired.

- **Well written and structured**: The paper is clearly structured and reads well. Particularly, the related work section is very strong.

### Weaknesses
I think this paper **is borderline**: The paper feels a lot about the _what_ is being done, and not really about the _why_ this may be useful. The paper does not really motivate the use of $P_{\text{uni}}$ outside of the image domain and would benefit a lot from a wider evaluation in different domains such as language and tabular and the interesting insights that can be generated there.

- **Limited Contribution**: The contribution of this paper is rather incremental in nature. The notions of _sufficiency_ and _necessity_ are quite established concepts. Here they are just added together (with a linear combination) and jointly optimized for. While the paper does make interesting findings because of this combined lens (see strengths). It falls short in motivating and placing the contribution well into the XAI research. It is unclear when from an XAI perspective this joint approach is superior to other techniques. The conducted experiments seem rather exemplary than confirmatory in this regard. Only a small selection of created images are presented **without** examples for the baseline explanation methods this work compares against. The contribution could be strengthened by providing a broader comparison in different domains and actually showing how the explanations of other methods differ with the the new perspective.

- **Doubt about the stability**: The experiments in the work show that sufficiency and necessity optimized together can lead to interesting insights. However, a critical aspect of retrieving these explanations is by optimizing ($P_{\text{uni}}$) in some form. This is again intractable like solving ($P_{\text{suf}}$) and ($P_{\text{nec}}$). The authors acknowledge this fact (line 215, footnote 1). However, the authors point to two references where one is un-published work (Kolek et al. 2021), and other is a workshop article (Kolek et al. 2022). This makes me doubt that the retrieved solutions to ($P_{\text{uni}}$) are easily retrievable for various models and feature spaces. Neither the paper nor the appendix discusses this issue further. While Experiment 6.1 is concerned with this fact, stability is evaluated only on a synthetic or tabular example with low feature dimensionality. While the remainder of the paper deals with image explanations, which seems to be the main motivation for this work, the stability is left undiscussed. 

- **Synthetic Setting is misused**: Given the above point stability is more interesting in higher-dimension settings (images, etc.). The synthetic environment would greatly benefit a _comparative study_ with other explanation methods. It would be interesting to see **how baselines fall short and be able to explain why** and then to show how the unification does not. This is in the current draft not done (also not in the exemplary setting of image explanations).

- **The Shapley-Perspective is Disconnected**: While I am glad about theoretical results linking this approach to game theoretic foundations (see strengths), Section 5.2 (connection of this method and Shapley) is quite disconnected to the rest of the paper. The results are presented technically but not put into context.

### Questions
- How stable are the retrieved explanations for the image case?

- What does it mean that _one searches for a player with a large lower bound_ in a two player game in practice. Can you put the results regarding the link of $P_{\text{uni}}$ into context. At the moment this connection is made and technically presented. It is not motivated or substantiated, why this is something good/bad or in-between.

### Soundness
4

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a novel measure to interpret predictions of black box machine learning models. Given a masking strategy for a model the authors define $\epsilon$-sufficient feature sets as sets whose masked prediction (mask= complement of S) deviates at most $\epsilon$ of the actual prediction with respect to some metric $\rho$ (deviation=$\Delta^{suf}$). In contrast, $\epsilon$-necessary feature sets are sets, where the masked prediction (mask=S) deviates at most $\epsilon$ from the fully masked prediction w.r.t $\rho$ (deviation=$\Delta^{nec}$). Given these notions, the authors aim to find the set $S$ with the smallest deviations. Instead of solving each problem individually, the authors propose to find a set that minimizes the weighted average $\Delta^{uni} := \alpha \Delta^{suf} + (1-\alpha) \Delta^{nec}$ with a hyper-parameter $0\leq \alpha \leq 1$, which they term "unified" problem, where the edge cases are the individual problems. The problem is further constrained, by finding a set with cardinality at most $\vert S \vert \leq \tau$. The main theoretical contribution is Theorem 4.1 that states the existence of $S$ with sufficiently small $\Delta^{uni}$, given sufficient and necessary solution and additional assumptions. Moreover, the solution satisfies conditional independence, if $f$ models the data-generating process (Corollary 5.1). Lastly, it is shown (Theorem 6.1) that the Shapley value of S treated as a joint player in the two-player game with S, [d]/S is bounded from below by $\Delta^{uni}$. In the experiments, the proposed is evaluated for different hyperparameter configurations on tabular data (6.1) and for image classification (6.2). For the restrictive setting in image classification, the authors propose an optimization objective that solves a relaxed version, which is specific to image classification, since exactly computing the objective is NP-hard. The authors conclude that the two proposed notions identify distinct aspects of predictions, which is showcased on examples for image classification.

### Strengths
1. The proposed necessary and sufficient explanations are an intriguing concept that complements existing approaches, such as the Shapley value that summarize "average contributions". Enriching the toolbox of interpretability methods with simple concepts is an important extension of existing work.
2. The paper is well-written, all theoretical claims are precisely stated and formally proven. The intuition behind the concepts are clear.
3. The proposed approximation method for image classification is interesting, but not sufficiently evaluated.
4. A first attempt to link the novel concepts to game-theoretic measures, such as the Shapley value, is promising.

### Weaknesses
1. **Limited discussion on computational aspects:** The paper introduces two interesting concepts, but the main limitation in practice is the optimization problem, which optimizes over all possible subsets (2^d), similar to the Shapley value. For the Shapley value, however, there exist efficient approximation techniques by evaluating the target for a collection of sampled subsets, which are unbiased and known to converge. In contrast, in Section 6.2 the authors propose approximation strategies for which no theoretical guarantees are given. The paper would highly benefit from such theoretical guarantees and a general approximation approach. Moreover, for the given applications, it should be carefully evaluated why these approximations yield appropriate solutions (see Q1 below).
2. **Limited link to other concepts:** Theorem 5.1 is a first step towards understanding connections to other methods, such as the Shapley value. However, this result is quite limited, since it considers a drastically reduced game of two players, instead of $d$ players, which does not give insights into the actual Shapley values that are usually computed for interpretability. The paper would strongly benefit from establishing such connections more carefully (see Q2 below), in particular given the claims made in the abstract.
3. **Comparison with existing attribution methods:** The authors claim that necessary and sufficient explanations yield more insights into explanations, which are undermined by some interesting examples in image classification. It remains unclear, how these methods compare to existing attribution methods. For instance, it would be helpful to formally state the difference between these concepts and carefully evaluate empirically which questions can be answered by the novel concept, which could not be targeted with existing methods. Moreover, some choices in the comparison are unclear to me (see Q3 below).
4. **Theorem 4.1:** The key assumption here is super-sufficient and super-necessary. I am not convinced that these properties are given in real-world examples (see Q4 below).
5. **Hyperparameters:** The method requires two hyperparameters $\alpha$ and $\tau$, which need to be chosen in advance, and have a high impact on the explanations, as shown by the experiments. It remains unclear how to choose these parameters in practice. It would be helpful to understand these choices better with sensible defaults.

### Questions
1. The proposed computation methods in Section 6.2. How well do they approximate the actual target? Could you do this analysis in a lower-dimensional setting, where ground-truths can be computed?
2. Do you have any insights on the method compared to the actual Shapley values of the model?
3. For the comparison of post-hoc explainability methods, what is the effect of the normalization? Is it negligible? Most methods already decompose the model's prediction, wouldn't it be sufficient to divide the attributions by the model's prediction to obtain normalized scores? Why don't you rely on the ranking of the attributions directly using $\tau$?
4. Is super-necessary and super-sufficient actually observed in practice? It seems counter-intuitive to me. For instance, for images, unmasking some parts of the image could lower the prediction significantly, since they could reveal a novel concept or another concept that contains the previously predicted concept.
5.  The purpose of the metric $\rho$ is unclear to me. It seems more intuitive to me to consider the model's output directly. What is the benefit of using the metric $\rho$? Why don't you use the model output directly, which is the common choice for local explanations? For necessary explanations, this also seems somewhat problematic: Consider a binary prediction, where the prediction is $\approx 1$, and the average prediction $f_\emptyset \approx 0.5$. Masking some features could substantially change the model's prediction to the opposite class, which would be captured with sufficient explanations. However, for necessary explanations, this would yield a similarly unsatisfying result (high $\Delta^{nec}), since the opposite class (prediction $\approx 0$) is equally far from the average prediction. Is this behavior intended? What is the reasoning behind it?
6. In Section 6.2. what are the resulting sizes of explanation sets that you find? Could you give some statistics on these for the datasets? Do you consider these sizes also in the comparison with post-hoc attribution methods? If so, in which way are they accounted for? E.g. I would expect to choose attributions of features such that the number matches with $\tau$?

**Minor**
- typo line 414, missing blank after "demonstrate"
- in Appendix A, the navigation displays "Proof of Theorem 6.1", while the section title is correctly referring to Theorem 5.1.

### Soundness
2

### Presentation
3

### Contribution
2
