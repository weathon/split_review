---
job_id: 5928dc33-1022-4b2a-9702-b085cd40780d
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Y6lVVJHiwN.pdf
paper: FedSGM: A Unified Framework for Constraint Aware, Bidirectionally Compressed, Multi-Step Federated Optimization
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on optimization, federated learning, constrained learning, compression, and reinforcement learning applications.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including problem setup, method, theory, experiments, and conclusion; despite serious clarity and correctness concerns, it is still a reviewable research paper rather than an obviously incomplete or non-scientific submission.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions or clear attempts to manipulate automated reviewing; the odd material on Pages 11–12 looks like document corruption or accidental inclusion rather than a prompt-injection attempt.

# Expected Review Outcome:
## Summary
This paper proposes FedSGM, a federated constrained optimization framework that combines switching-gradient style primal updates with multiple local steps, bidirectional compression with error feedback, and partial client participation. The paper presents convergence guarantees for hard switching and a soft-switching variant, and evaluates the approach on Neyman-Pearson classification and a constrained CartPole CMDP task.

## Strengths
The paper tackles a meaningful problem formulation. Combining functional constraints, local updates, biased compression with error feedback, and client subsampling is a practically relevant direction for federated learning, and the paper is trying to close a genuine gap between constrained optimization and realistic FL system assumptions.

The high-level algorithmic idea is appealing. In particular, using switching-gradient style primal-only updates instead of introducing dual variables or penalty schedules is conceptually clean, and the motivation for avoiding projection or nested inner solves is reasonable in federated settings with limited compute and communication.

The paper does make a serious effort on theory, not just heuristics. There are explicit theorems for hard and soft switching, and the main text gives rates that try to isolate the effects of local updates, compression, and partial participation. Even though I have concerns about the derivations and consistency of the statements, the intended scope is broader than many standard constrained FL papers.

I appreciated the geometric discussion in Section 3.2 about oscillations under hard switching. The introduction of \(K_{\mathrm{glob}}\) and \(K_{\mathrm{loc}}\) gives an intuitive lens for why switching near the feasibility boundary may be unstable under heterogeneity. This is one of the more interesting parts of the paper conceptually.

The experiments do provide some evidence that soft switching can reduce instability relative to hard switching. In **Figure 1** on Page 7, the soft-switching curve for the constraint appears less oscillatory around the threshold than the hard-switching counterpart, which supports the practical motivation in Section 3.2. Likewise, the top and bottom rows of **Figure 2** on Page 8 are useful because they show the sensitivity to local steps and compression, rather than only reporting a single tuned setting.

The CMDP experiment is a reasonable stress test for the proposed idea. The reward-cost tradeoff shown in **Figure 3** and the partial participation effect in **Figure 4** at least attempt to demonstrate behavior beyond a small convex benchmark.

The paper includes a quantitative summary table for compression effects in the RL setup. **Table 1** on Page 9 is useful because it distinguishes feasibility from reward, and it makes clear that some compressed settings are safe but much less performant, for example \(K/d=0.25\), while quantization seems to preserve final reward much better. That kind of breakdown is more informative than a single scalar metric.

## Weaknesses
I have substantial concerns about the mathematical consistency of the paper, and these are not cosmetic. Several theorem statements, algorithm descriptions, and proof details do not line up with each other.

1. **The treatment of constraints in the theorem statements is inconsistent, and in one place incorrect.** In **Theorem 1** on Page 4, the full-participation result claims \((ii)\; g(\bar w)-g(w^\*)\le \epsilon\). But for a constrained problem of the form \(g(w)\le 0\), the natural feasibility statement is \(g(\bar w)\le \epsilon\), not a bound relative to \(g(w^\*)\). This is especially problematic because later the paper informally interprets the result as feasibility of the averaged iterate, and in other places, including the introduction and the partial-participation statement, the paper switches back to \(g(\bar w)\le \epsilon\). Since \(g(w^\*)\) need not be zero, the theorem as written is not the same guarantee. This matters because the headline claim is about certifying feasibility, and the formal statement does not consistently match that claim.

2. **The role of the feasible set \(\mathcal X\) is contradictory across the paper.** The main problem in Equation (1) on Page 1 is posed over \(w\in \mathcal X\), and Algorithm 1 updates local models by plain gradient steps \(w_{j,\tau+1}^t = w_{j,\tau}^t - \eta \nu_{j,\tau}^t\) with no projection in the local loop. Yet the appendix theorems repeatedly switch assumptions between \(\mathcal X\subset \mathbb R^d\) compact convex and \(\mathcal X=\mathbb R^d\), for example **Theorem 3** on Page 24 and **Theorem 6** on Page 32 assume \(\mathcal X=\mathbb R^d\), while **Theorem 4** on Page 27 uses projected global updates via \(\Pi_{\mathcal X}\). These are materially different algorithms. If the method is really “projection-free” as emphasized throughout Pages 1–3, then introducing projection in the partial-participation proofs is a notable change in the algorithmic model. If \(\mathcal X=\mathbb R^d\), then Assumption 2 about compactness is not in force. Right now the reader is left to guess which setting the main claims actually cover.

3. **Algorithm 1 is underspecified and, in places, wrong at the level of notation.** On Page 5, line 16 writes
\[
\nu_{j,\tau}^t \gets (1-\sigma_t)\nabla f_j + \sigma_t \nabla g_j,
\]
but the gradients are missing evaluation points; it should presumably be \(\nabla f_j(w_{j,\tau}^t)\) and \(\nabla g_j(w_{j,\tau}^t)\). That is not just a typographical nuisance because the proofs depend on local iterates \(w_{j,\tau}^t\). Similarly, the algorithm header introduces \(x_0\), \(e_j^0\), compressors, and server/client residuals, but the actual pseudocode shown in the main paper stops at line 19 and does not include the compression/error-feedback steps at all. For a paper whose title explicitly emphasizes “bidirectionally compressed” optimization, this is a serious omission in the main text. Theorems are stated for Algorithm 1, but the main-paper Algorithm 1 does not actually specify the bidirectional EF mechanism that those theorems are about.

4. **There are visible inconsistencies between main-text theorem constants and appendix theorem constants.** For example, the full-participation hard-switching \(\Gamma\) in **Theorem 1** on Page 4 is
\[
\Gamma = 2E^2 + \frac{2E\sqrt{1-q}}{q} + \frac{4E\sqrt{10(1-q_0)}}{q_0 q},
\]
while the uncompressed derivation in **Theorem 3** on Pages 24–26 leads to \(\Gamma = \frac12 E + 1 + \frac13 E^2\), and the compressed result in **Theorem 6** on Pages 32–36 again uses a different decomposition. A reader can accept different \(\Gamma\) definitions across different settings, but here the paper frequently presents one theorem in the main text as if it is a streamlined version of the appendix proof, while the details do not actually match cleanly. The soft-switching theorem in the main text is even worse: **Theorem 2** on Page 7 displays a malformed \(\Gamma\) expression, “\(\Gamma = 2E^2 + \underbrace{4E\sqrt{10(1-q_0)}}_{q} + \underbrace{q_0q}_{q}\)”, which is mathematically nonsensical as written. That directly weakens confidence in the claimed rate.

5. **The partial-participation concentration term is suspiciously inconsistent in the exposition.** On Page 6, the discussion states that the concentration radius is of the form
\[
\epsilon \gtrsim \text{optimization error} + \sigma \sqrt{2\log(6T/\delta)/m^2},
\]
which scales like \(1/m\), not \(1/\sqrt m\). Under Assumption 4, the constraint gap is \(\sigma^2/m\)-sub-Gaussian, so the natural deviation scale is \(O(\sigma/\sqrt m)\), which is what later lemmas use. This may be “just” a prose error, but it lands exactly in the paper’s central message about decoupling optimization and sampling noise. If the main interpretation paragraph gets the scaling wrong, it is hard to fully trust the theorem presentation.

6. **Some proofs contain concrete mathematical mistakes or at least careless substitutions that change the object being bounded.** For instance, in **Lemma 1** on Page 18, the second case for \(t\in \mathcal B\) writes
\[
TermA = -2\eta \langle w_t - w_{j,\tau}^t, \nabla f_j(w_{j,\tau}^t)\rangle \le \cdots
\]
even though the update in \(\mathcal B\) is supposed to use \(\nabla g_j\), not \(\nabla f_j\). This is exactly the sort of copy-paste mistake that may look minor but matters in a switching method, because the proof splits cases precisely according to whether the objective or constraint gradient is used. There are several such issues throughout the appendix, enough that I do not have high confidence the full derivations have been checked carefully.

7. **The claimed connection to prior work is overstated, and the novelty positioning is not fully convincing from the main paper.** The paper repeatedly says this is the first unified framework for constraints, compression, local updates, and partial participation. But the appendix itself references very closely related switching-gradient work, and the paper’s own framing suggests that parts of the contribution are extensions of known ingredients rather than a fundamentally new optimization principle. The issue is not that the extension is uninteresting, it is that the main paper’s “first unified framework” language is stronger than the evidence provided in the main text. The reader needs a more precise delineation of what exactly is new relative to recent switching-gradient FL work with compression and to bi-directional compressed FL more broadly.

8. **The experimental evidence is thinner than the breadth of the claims.** The core theory is for convex constrained optimization, but the experimental section gives one small logistic-regression NP classification example and one non-convex RL example. There is no convincing bridge between these. The NP task is based on the breast cancer dataset with only \(569\) samples, split IID across \(n=20\) clients according to Appendix F.2, which is a very mild federated setting. This does not really stress heterogeneity, even though heterogeneity is central to the soft-switching motivation in Section 3.2. The RL experiment is more heterogeneous, but it does not test the convex theory at all. So the paper ends up under-supporting both sides: the convex theory is not validated on challenging convex FL tasks, and the practical non-convex claims are not theoretically covered.

9. **The experimental baseline selection is weak in the main paper.** For the main experimental section, there is essentially no direct comparison against constrained FL baselines, primal-dual methods, or even a carefully tuned penalty-based approach in the core pages. The appendix later includes a comparison against a penalty baseline in **Figure 6** and a fairness experiment in **Figure 7**, but the main text does not present these as central evidence. Given the paper’s very strong claims about avoiding penalty tuning and outperforming practical alternatives, this omission matters. A paper making “unified foundation” claims should not rely mainly on self-comparisons between hard and soft switching plus centralized references.

10. **The interpretation of the figures is somewhat selective and sometimes weaker than the text suggests.** In **Figure 2** on Page 8, the top row does show diminishing gains as \(E\) increases, but it also suggests fairly noticeable instability in the constraint curves even under soft switching for larger \(E\). The discussion mentions this, but the overall take-away in the paper still reads as overly positive. Similarly, **Figure 3** for CMDP does not convincingly show a clean dominance pattern; the trajectories are noisy, and the reward advantage of one variant over another is not stable enough to support strong claims. These figures suggest promise, not a definitive empirical case.

11. **Table 1 on Page 9 raises questions that the text does not really answer.** The table shows that Top-\(K\) with \(K/d=0.5\) reaches only reward \(131.6\) after 500 rounds, far below the no-compression and quantized variants around \(199\), and \(K/d=0.25\) barely learns at all. That is not a minor slowdown, it is a major degradation. Yet the surrounding discussion frames the results mostly as evidence that the method “stably satisfies constraints and maximizes episodic reward.” That statement is too broad given the table. The method appears sensitive to sparsification, and the paper should discuss when bidirectional EF is insufficient in practice rather than smoothing this over.

12. **Presentation quality is noticeably below the standard expected for a theory-heavy ICLR paper.** Beyond local typos, there are malformed formulas, duplicated or broken references, and apparent document corruption on **Pages 11–12**, where unrelated-looking figures and text fragments appear (“The performance of the proposed model on the 2024-2025 ICLR 2026...” ). Even if this is an assembly error, it affects readability and professionalism. A paper asking reviewers to trust a long technical appendix needs much tighter presentation than this.

13. **The main text leaves important implementation details to the appendix while still making strong practical claims.** For example, the exact bidirectional EF update, residual handling, and compressor simulation details are not clear enough from the main algorithm. In **Table 1**, Top-\(K\) and quantization are “simulated” in a simplified way on Page 9, rather than being implemented as actual datatype conversion or bandwidth-constrained transmission. That is acceptable for exploratory experiments, but it weakens the practical interpretation of the communication-efficiency claims.

14. **The soft-switching theorem is incomplete relative to the overall framework claim.** **Theorem 2** in the main paper only addresses full participation. The abstract and title present a unified framework spanning partial participation as well, but the soft-switching guarantees under partial participation are not established in the main text. If the most practically attractive part of the method, soft switching, lacks the same coverage as hard switching, the “unified” claim should be stated more carefully.

## Questions
1. The main text and appendix are not consistent about whether the algorithm is projection-free or whether the server performs a projection onto \(\mathcal X\), especially comparing **Algorithm 1** and **Theorem 4** on Page 27. Which algorithm is actually claimed in the main theorems? Please provide a single consistent update rule and explicitly state whether \(\Pi_{\mathcal X}\) is used anywhere.

2. In **Theorem 1**, should the feasibility statement be \(g(\bar w)\le \epsilon\) rather than \(g(\bar w)-g(w^\*)\le \epsilon\) in the full-participation case? If not, please explain why the stated form is the right notion of feasibility and how it supports the claims made in the abstract and introduction.

3. Please clarify the exact bidirectional compression/error-feedback mechanism in the main paper. As written, **Algorithm 1** does not actually specify the compression steps, residual updates, or server-side decompression logic that the theorems analyze. A concise but complete main-text algorithm would increase confidence substantially.

4. Can the authors provide a cleaned-up and internally consistent version of the soft-switching theorem? In particular, the \(\Gamma\) expression in **Theorem 2** on Page 7 appears malformed. I would like to know the exact statement the authors intend, and whether the theorem is truly different from the hard-switching bound beyond the weighting scheme.

5. For the NP classification experiment, can the authors add a genuinely heterogeneous data split rather than the IID split described in Appendix F.2, and compare hard vs soft switching there? That would better test the geometric-heterogeneity motivation from Section 3.2. Right now the main convex experiment is too mild to validate claims about client-induced skewness.

6. For the RL experiments, can the authors include stronger baselines in the main paper, not just appendix figures? At minimum, a tuned penalty-based FL baseline and one relevant constrained optimization baseline would help contextualize whether the observed gains are from switching per se or from implementation choices.

7. Please explain the discrepancy between the optimistic compression narrative and **Table 1**. Why does Top-\(K\) with \(K/d=0.5\) or \(0.25\) perform so much worse than quantization despite the theory emphasizing general biased compressors? Is the theory too coarse to distinguish these regimes, or is the implementation particularly unfavorable to sparsification?

8. Could the authors clarify the concentration discussion on Page 6, where the scaling is written like \(O(1/m)\) instead of \(O(1/\sqrt m)\)? If this is a typo, it should be fixed because it appears in an interpretive paragraph about the main theorem.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns are apparent from the submission itself. The applications include fairness and safety-constrained learning, which are socially relevant, but the paper does not introduce a dataset, deployment system, or user-facing study that would warrant a dedicated ethics escalation based on the main text alone.

## Soundness Rating
2: fair. The paper has a serious theoretical ambition and some plausible ideas, but the central claims are weakened by inconsistent theorem statements, underspecified algorithms, and multiple mathematical/presentation errors.

## Presentation Rating
1: poor. The paper is difficult to trust in its current form because of malformed equations, inconsistent notation, incomplete pseudocode, and visible document corruption on later pages.

## Contribution Rating
2: fair. The problem tackled is important and the attempted combination of ingredients is relevant, but the paper does not yet provide a sufficiently reliable or clearly positioned contribution at ICLR standard.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The paper is aiming at a meaningful and practically relevant synthesis, and there are some promising ideas, especially around soft switching and constrained FL with communication limits. However, there are too many inconsistencies in the mathematical statements, too much underspecification in the actual algorithm, and the empirical case is not strong enough to compensate. With a careful revision, this could become a solid paper, but in its current form I do not think it clears the bar.

## Reviewer Confidence
4: confident. I am confident in the overall assessment, and I checked the main claims, equations, and theorem statements carefully enough to believe the identified issues are substantive rather than stylistic.