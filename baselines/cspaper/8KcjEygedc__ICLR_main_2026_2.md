---
job_id: f17b194c-5d95-4243-9fc4-56763460f04f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 8KcjEygedc.pdf
paper: Why Less Is More (Sometimes): A Theory of Data Curation
main_score_norm: 0.8
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, primarily as a learning theory paper on scaling laws, data curation, and high-dimensional generalization, with supporting experiments in vision and discussion of LLM reasoning.

## Minimum Quality
Pass ✅. The paper contains the expected scientific structure, including abstract, introduction, related work, theoretical methodology, experiments/results, and conclusion; despite several clarity and technical issues, it clears the bar for full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden instructions, suspicious reviewer-targeting text, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies when training on a curated subset of data can outperform training on all available data. In a high-dimensional Gaussian binary classification model with pruning oracles, the authors derive asymptotic test-error formulas for both label-agnostic and label-aware curation, characterize regimes where “keep hard” or “keep easy” is optimal, and connect the analysis to model collapse under label shift. The paper also includes empirical illustrations on synthetic data and ImageNet, plus a discussion of recent LLM reasoning results through the lens of the proposed theory.

## Strengths
The main strength is that the paper tackles a timely and genuinely important question, namely when aggressive data curation bends or even reverses the usual “more data helps” intuition. This is a useful problem for the ICLR community because the field is currently flooded with empirical claims about filtering, pruning, synthetic data, and “less is more”, but much of that discussion is still heuristic.

The theory is ambitious and, at a high level, well motivated. The setup in Sections 2 and 3 cleanly separates three roles, the generator \(w_g\), the oracle \(w_o\), and the ground truth \(w_*\), which is a sensible abstraction for pseudo-labeling, verification, and self-training. The distinction between label-agnostic curation in Eqn. (5) and label-aware curation in Eqn. (6) is also valuable, because it lets the paper speak both to classical margin-based pruning and to more verification-style filtering pipelines.

I also liked that the paper aims for exact asymptotic error formulas rather than only qualitative monotonicity statements. In particular, Theorem 1 and Theorem 3 are positioned as explicit scaling-law characterizations of test error under pruning, and that is a stronger contribution than simply observing that some pruning policy can help in some cases.

The figures do a good job conveying the paper’s main message. **Figure 1** is especially effective in illustrating the intended phase structure: the bottom-left panel is the only regime where aggressive pruning beats full-data training, while the other three panels revert to the standard “more is more” behavior. Even before digging into the appendices, that figure gives a crisp visual summary of the claimed mechanism, and the close match between solid and dashed curves there is an important piece of evidence that the asymptotic theory is not totally detached from finite-sample behavior in the toy setting.

The ImageNet section, while not exhaustive, is directionally interesting. **Figure 2** presents a visually clear crossover between “keep easy” and “keep hard” as the initial dataset size changes, which is precisely the sort of phenomenon the theory predicts. This is a much stronger empirical story than simply showing one curated subset beating one uncurated baseline.

The paper also does a decent job using tables to support its broader narrative. **Table 1** and **Table 2** are useful in that they make the central paradox concrete: aggressive curation helps average AIME performance in one setting, while larger training sets help on harder question slices in another. Even though these are literature-reported results rather than the authors’ own experiments, the juxtaposition is informative and helps explain why the theoretical question is worth asking.

Finally, the paper is relevant beyond its exact assumptions. Even if the Gaussian linear model is stylized, the generator-oracle-ground-truth decomposition is conceptually useful, and the paper provides a reasonably coherent lens for thinking about data filtering, pseudo-labeling, and collapse mitigation.

## Weaknesses
My main reservation is that the paper sometimes overstates how cleanly the theory has been nailed down in the main text, while several key definitions and logical links are either underspecified there or internally inconsistent.

1. **There is an important inconsistency around the central optimal-pruning result, namely Theorem 2 on Page 5.**  
   The theorem states:
   - Part (A): if the generator is excellent, \(\rho \to 1\), and the pruner is excellent, \(\rho_* \to 1\), then keep-hard is optimal.
   - Part (B): if the generator is poor, \(\rho < 1\), but the pruner is excellent, \(\rho_* \to 1\), then keep-easy is optimal.  
   However, in the proof in Appendix G.3, the argument labeled “Part (A)” proceeds by taking \(\rho_* = 1\), and the argument labeled “Part (B)” proceeds by taking \(\rho = 1\). That is not a cosmetic typo, because \(\rho\) and \(\rho_*\) play very different conceptual roles throughout the paper. As written, the proof and theorem statement do not align cleanly. Since Theorem 2 is one of the headline claims of the paper, this matters a lot. The authors need to explicitly reconcile the assumptions used in the proof with the theorem statement in the main paper, and state the exact conditions under which keep-hard versus keep-easy is optimal.

2. **Eqn. (13) on Page 5 appears mathematically inconsistent or at least incorrectly transcribed.**  
   For label-aware curation, the paper defines
   \[
   p:=\mathbb{P}(p_i=1),\quad \gamma:=\mathbb{E}[(y_i^o)^2p_i],\quad \beta:=\mathbb{E}\left[\frac{\partial f_i}{\partial z_i^o}\right],\quad \tilde{\beta}:=\mathbb{E}\left[\frac{\partial f_i}{\partial z_i^o}\right].
   \]
   Here \(\beta\) and \(\tilde{\beta}\) are literally identical. But later, Table 3 in the appendix gives different formulas for the two constants in the label-aware case, and Theorem 3 relies on them as distinct quantities. This is not a minor notation annoyance, because these constants feed directly into \(m_0\), \(\nu_0\), and ultimately the test error. The main paper must fix this expression. Right now, a careful reader cannot reconstruct the claimed label-aware formula from the main text.

3. **The main theorem statements are too compressed for the level of claim the paper is making.**  
   In Theorem 1 on Page 4, the test error depends on \(m\), \(\tilde m\), and \(r\), but these objects are only described vaguely as “functions explicitly determined by the constants in Eqn (8)” and deferred to the appendix. For a paper whose core contribution is supposedly “exact scaling law curves,” the main paper gives surprisingly little of the actual functional form. I am not asking for a full appendix-level proof in the main text, but at least the explicit isotropic formulas, or a short display defining
   \[
   m(z),\quad \tilde m(z),\quad r(z),
   \]
   should have been included in the main theorem section. As written, the main result is difficult to verify from the main paper alone, and it reads more like a pointer to appendix machinery than a self-contained theoretical contribution.

4. **The empirical validation in the main paper is not as strong as the rhetoric suggests.**  
   The paper repeatedly claims to “empirically confirm” the theory, but the main paper’s direct validation is somewhat selective. **Figure 1** compares “keep hard” against “random” across four regimes, which supports the broad message, but it does not directly test the theorem’s stronger claim that the optimal strategy switches between “keep hard” and “keep easy” depending on generator quality. The reader has to wait until **Figure 2** on ImageNet for an actual KH-versus-KE crossover, and even there the setup is much less controlled than the synthetic theory. In other words, the main-paper empirical story is one step weaker than the theorem headline.

5. **The LLM section is mostly interpretive, not experimental, and the paper should be more explicit about that.**  
   **Table 1** and **Table 2** on Page 7 are not produced by this paper; they are aggregated from prior work. That is fine as motivation, but the wording in Section 4.2 risks making the contribution sound more empirically grounded than it is. These tables show that two phenomena coexist in the literature, but they do not test whether the paper’s variables \(\rho\), \(\rho_*\), and \(\rho_g\) actually explain those results. Since the paper does not operationalize those quantities in the LLM setting, the “reconciliation” remains qualitative. This matters because the paper leans heavily on LIMO and s1 in the introduction and abstract, so the practical relevance claim should be stated with more restraint.

6. **The ImageNet experiments are suggestive, but the main paper leaves too many implementation details unspecified to fully assess whether the comparison is fair or how exactly it maps onto the theory.**  
   In Section 4.3 and **Figure 2**, the paper says it uses a pre-trained model as both generator and pruner to create and select from a pseudo-labeled dataset, and compares “keep easy” against “keep hard.” But the main paper does not specify, in the actual experiment section, how difficulty is defined in the multiclass setting, what score is thresholded, how thresholds are chosen to match pruning fractions, whether pseudo-label confidence is entangled with correctness filtering, or how many times the experiments were repeated. The appendix adds training details, but the core curation protocol itself should be clear in the main paper. Without that, it is hard to know how much of **Figure 2** reflects the theory and how much depends on a particular operationalization of “easy” and “hard.”

7. **The model-collapse claim is intriguing but currently under-controlled.**  
   **Figure 3** shows that repeated training on all pseudo-labeled data degrades performance, while keeping “hard” examples stabilizes it. That is a nice picture, but the paper does not convincingly isolate whether the gain comes from the specific theory-guided pruning principle or from incidental effects such as changed effective sample size, implicit regularization, or reduced noise amplification. A stronger case would compare against more baselines at matched compute and matched retained-set size, including random pruning and keep-easy pruning in the recursive loop. As shown, the figure supports a promising claim, but not yet a definitive one.

8. **There are several smaller exposition issues that accumulate.**  
   - The paper flips between intuitive prose and technical objects without always keeping notation tight.  
   - The naming of “keep easy” and “keep hard” is confusing in the appendix. On Page 37, Eqn. (81) defines \(q_{\mathrm{KE}}(t)=1[|t|\ge \alpha]\), which actually retains large-margin points, while Eqn. (82) defines \(q_{\mathrm{KH}}(t)=1[|t|\le \alpha]\), which retains small-margin points. This is opposite to the main-text convention on Page 3. That is not a harmless slip, because the entire paper revolves around the distinction.  
   - There are also formatting/organization glitches, for example the malformed “Future Directions” list on Page 9. None of these kills the paper, but they do make a theory-heavy submission harder to trust than it should be.

9. **The paper’s empirical positioning relative to compute-aware data filtering is incomplete.**  
   The framing focuses on “less vs more data,” but some closely related work studies data filtering as a compute-aware scaling problem rather than a pure subset-selection phenomenon. That omission matters because part of the practical value of pruning is exactly the tradeoff between retained data, training budget, and quality. The current presentation sometimes sounds more universal than the actual theoretical regime justifies.

Overall, I think the paper has a real idea and a meaningful contribution, but the manuscript needs more discipline around theorem statements, notation, and the precise scope of its empirical claims. Right now, the core story is stronger than the paper’s exact execution.

## Questions
1. **Please clarify the mismatch between the statement and proof of Theorem 2.**  
   In Appendix G.3, the proof steps for parts (A) and (B) seem to use different limiting assumptions than those stated on Page 5. Which version is the correct theorem? A precise corrected statement would materially increase my confidence.

2. **Can you correct Eqn. (13) and explicitly define the distinct label-aware constants used in Theorem 3?**  
   As written, \(\beta\) and \(\tilde{\beta}\) are identical in Eqn. (13), which seems inconsistent with Table 3 and the appendix derivation. Please state the exact main-text formula that should replace Eqn. (13).

3. **Can you provide a main-text version of the isotropic formulas for \(m(z)\), \(\tilde m(z)\), and \(r(z)\)?**  
   Even a short boxed equation would help substantially. Right now, the “exact” nature of the scaling law is hard to inspect from the main paper.

4. **For the ImageNet experiments, how exactly are “easy” and “hard” examples defined in the multiclass pseudo-label setting?**  
   Is the score based on confidence, logit margin, entropy, top-1 probability, or something else? How are pruning thresholds selected, and are the comparisons repeated over multiple random seeds? A precise answer here would make Figure 2 much more compelling.

5. **For Figure 3, did you compare against random pruning and keep-easy pruning across recursive rounds, under matched retained-set size and matched total optimization steps?**  
   If such controls exist, they would greatly strengthen the model-collapse mitigation claim.

6. **What is the strongest practical claim you believe the paper supports for LLM reasoning?**  
   Given that Section 4.2 uses literature tables rather than experiments from this paper, I would encourage a more careful delineation between “theory is consistent with these observations” and “theory is validated on this domain.” Please clarify how far you think the current evidence really goes.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethics concerns are raised by the paper itself. The work is primarily theoretical and empirical on standard ML datasets, and I did not identify a concrete issue requiring ethics escalation based on the main paper.

## Soundness Rating
3: good. The core theoretical direction is promising and much of the analysis appears technically serious, but there are nontrivial inconsistencies in theorem statements and notation, especially around Theorem 2 and Eqn. (13), that reduce confidence in the paper’s current presentation of its claims.

## Presentation Rating
3: good. The paper is readable and the high-level story is clear, with effective figures, but several notation inconsistencies, underspecified definitions, and a few organizational glitches prevent a higher score.

## Contribution Rating
3: good. The paper makes a meaningful contribution by proposing a principled theory for when data curation helps, and the generator-oracle-ground-truth perspective is useful; however, the empirical bridge to practical settings is still somewhat lighter than the headline framing suggests.

## Overall Rating
8: Accept, good paper (poster). I see clear value in this paper and think it makes a worthwhile contribution to ICLR, but it is not a fully polished theory paper yet. The main reason I am positive rather than borderline is that the central question is important, the theoretical framing is useful, and the paper gives a coherent explanation for an otherwise confusing set of empirical observations. The main reason I am not higher is that some theorem statements and formulas need cleaning up, and the practical validation remains suggestive rather than airtight.

## Reviewer Confidence
4: confident. I am confident in the overall assessment and in the main issues identified, especially the statement/proof/notation inconsistencies and the scope of the empirical evidence, though I have not rederived every appendix proof line by line.