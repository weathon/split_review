Now I have a complete picture. Let me produce the final consolidated review.

## Summary

This paper demonstrates that MLPs and MLP-Mixers can learn in-context on synthetic regression and classification tasks at performance levels comparable to Transformers when matched for total training compute (PFLOPs), and that vanilla MLPs outperform Transformers on three relational reasoning tasks (match-to-sample, sphere oddball, line oddball) with better out-of-distribution generalization. The core empirical finding—that ICL is not unique to attention-based architectures—is supported by controlled experiments with Bayes-optimal baselines and IWL-to-ICL transition analyses across architectures.

## Strengths

- **Compute-controlled comparison shows MLPs match Transformer ICL performance at scale.** Figure 1c plots MSE vs. total training compute (PFLOPs) on unrestricted ICL regression; at large compute, MSE is "approximately equal across all architectures" (line 30 caption, lines 48–49). This directly supports the claim that MLPs learn in-context competitively with Transformers given the same compute budget, going beyond prior work that nearly exclusively studied Transformers.

- **IWL-to-ICL transition demonstrated in MLPs.** Figures 1e–f (regression) and 1j (classification) show that as data diversity $k$ increases, MLPs and MLP-Mixers transition from in-weight learning (dMMSE curve) to in-context learning (Ridge curve), just as Transformers do (lines 53–54). Prior work (Raventos et al., Reddy et al.) established this transition only for Transformers; showing it holds for MLPs challenges the assumption that attention is required for this phenomenon.

- **MLPs outperform Transformers on relational reasoning tasks with better OOD generalization.** On match-to-sample (Figure 3b), sphere oddball (Figure 3e), and line oddball (Figure 3i), MLPs achieve better loss with less compute than Transformers. Crucially, Figures 3c and 3f show MLPs generalize perfectly to OOD radii and perturbation distances while Transformer performance degrades. On sphere oddball, the Transformer's logit for the oddball "asymptotes to a flat value" while MLPs learn "strictly increasing relationships" (lines 102–103)—evidence that the Transformer and MLP learn qualitatively different solutions.

- **Identifies a sharp architectural boundary in context-length sensitivity.** Figure 1d shows that vanilla MLPs fail catastrophically on regression with context lengths beyond $2^6$, approaching the MSE of a zero estimator (line 51), while MLP-Mixers maintain Bayes-optimal MSE even at long contexts. This dissociation between two MLP-based architectures is a precise, non-obvious finding that prior Transformer-only work could not reveal.

- **Bayes-optimal and random baselines throughout.** Every experiment includes a theoretical lower bound (Bayes optimal Ridge MSE, Figure 1c–d) or a random-guess baseline (Figure 1h, Figures 3f and 3j), calibrating how close each architecture is to the information-theoretic optimum and making comparisons quantitatively meaningful.

## Weaknesses

### Fatal

None.

### Major

- **The relational tasks where MLPs most clearly outperform Transformers are very low-dimensional (2D inputs, 5–6 context points), and the outperformance on these narrow toy problems does not carry as much weight as the paper's framing suggests.** The match-to-sample task learns an argmax over 2D dot products on a circle; the sphere oddball task learns to pick the point farthest from a centroid. These are simple geometric functions that any sufficiently wide MLP can approximate. That a Transformer (which must route information through attention, positional encoding, etc.) is less compute-efficient on such small problems is not surprising and does not strongly support broad claims about MLP superiority for ICL. The paper is honest about the synthetic nature of these tasks in the limitations section (line 124), but the main text's claim that "MLPs outperform Transformers" on relational tasks (used multiple times as a headline result) would benefit from more measured framing that acknowledges the narrowness of the evidence base.

### Minor

- **The paper's "ICL" framing for MLPs downplays a qualitative difference from Transformer ICL that readers will find important.** The MLP requires a fixed context length $L$ baked into its input dimensionality (line 44). While the paper tests an autoregressive variant (results "unchanged," line 44, referring to the appendix), the primary experiments and core architectural requirement are fixed-length. A Transformer can process arbitrary-length sequences up to its maximum through attention; an MLP trained on $L=64$ cannot handle $L=100$ without architectural retraining, and indeed Figure 1d shows MLPs fail entirely beyond $2^6$ context points. The paper acknowledges this empirically but does not fully grapple with whether a model with a fixed-context-length input can be said to perform the same kind of "in-context learning" that makes the phenomenon interesting in Transformers. This does not invalidate the findings, but the central contribution would be strengthened by directly addressing this framing concern rather than treating the length sensitivity as a secondary finding.

- **The IWL-to-ICL transition occurs at somewhat smaller $k$ for Transformers than for MLPs** (line 53: "The Transformer makes this transition at a somewhat smaller $k$ than the MLP models"), which is noted but not analyzed. This suggests Transformers have a meaningful inductive bias advantage for ICL even on these synthetic tasks. The paper's framing emphasizes parity, but the data show consistent efficiency advantages for Transformers in data-limited regimes, consistent with the "bitter lesson" framing the authors themselves invoke.

- **The comparison between architectures relies on a compute-matching methodology whose details are deferred to the appendix.** The paper states models are compared "based on the total compute required for training (measured in PFLOPs)" and "we select the best model configuration as measured by loss, keeping compute cost equal across architectures" (line 17). This is a principled approach, but the main text provides no architectural specifics (depths, widths, activations, search procedure, optimizer settings) needed to evaluate whether the matching is fair. While I cannot penalize the paper for stripped appendix content, the reliance on opaque appendix details for a claim that hinges on fair comparison is a structural weakness in the presentation.

### Trivial

- None.

## Nice-to-Haves

- A mechanistic analysis of what the MLP actually learns internally (e.g., does it approximate a least-squares solver or just learn a direct function mapping?) would substantially strengthen the claim that MLPs do ICL rather than simply learn complicated function approximators. The Transformer ICL literature has such studies (von Oswald et al., Akyürek et al.); similar probing for MLPs would be valuable.

- An analysis of why MLP-Mixer is robust to context length when vanilla MLP is not (Figure 1d). This architectural dissociation is noted but not explained, and understanding it could reveal something fundamental about how input structure affects ICL capability.

## Removed Points

- **Criticism about missing architectural details / compute fairness methodology.** The harsh critic argued that the main text provides "almost no architectural details needed to evaluate its fairness" and speculated about potential unfairness. These details are in the appendix, which the parser strips. Per guidelines: remove criticisms about missing appendix content. The appendices exist in the original submission.

- **Criticism that the RB MLP comparison's role is unclear.** The paper clearly explains the RB MLP's purpose (lines 79, 87–88, 98) as a gold-standard comparison with hand-crafted relational features. The critic's confusion is a misreading.

- **Criticism about statistical significance / CI overlap.** The paper reports 95% confidence intervals from 5 replications, which is standard practice. The generic suggestion that claims should be "quantified relative to variance" is not a specific identified problem.

- **Criticism about the autoregressive variation being deferred to appendix.** Per guidelines: remove criticisms about appendix-deferred content.

- **Strength Finder strengths about "addressing an important problem" or generic framing.** All retained strengths are concrete and grounded in specific figures/claims; no generic strengths were kept.

## Novel Insights

None beyond the paper's own contributions. The key novel insight—that MLPs can learn in-context competitively with Transformers on synthetic ICL tasks—is the paper's own contribution, not something synthesized from the reviews.

## Suggestions

1. **Reframe the relational task results more carefully.** The headline "MLPs outperform Transformers on relational tasks" should be qualified with the observation that these are very low-dimensional (2D, 5-6 point) tasks where the MLP's function-approximation advantage is expected. The paper would be stronger if it positioned these results as "on simple relational tasks" rather than implying general superiority.

2. **Address the fixed-context-length framing directly in the main text.** Add a paragraph discussing what it means for an MLP to "learn in-context" when context length must be baked into the architecture, and how this differs from the flexible-length ICL of Transformers. This would preempt the most common reader objection.

3. **Analyze the Transformer advantage in data-limited settings.** The paper notes Transformers transition to ICL at lower data diversity (line 53). This is a genuine architectural advantage worth examining explicitly, not just mentioning in passing.

4. **Move the architectural details / compute-matching methodology to the main text** (or at minimum, ensure the appendix description is comprehensive and cross-referenced clearly in the main text), since the entire comparison framework hinges on its fairness.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>