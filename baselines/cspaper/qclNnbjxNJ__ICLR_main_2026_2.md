---
job_id: 846e6a83-9fca-4e8c-9bc5-b2c3ef965d33
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: qclNnbjxNJ.pdf
paper: Characterization and Learning of Causal Graphs with Latent Confounders and Post-treatment Selection from Interventional Data
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope, specifically causal reasoning and learning from interventional data, with applications to biology.

## Minimum Quality
Pass ✅ The paper contains the expected scientific components, including abstract, introduction, methodological development, theoretical results, experiments, and conclusion. While the exposition and some technical statements are rough in places, the work is sufficiently complete, nontrivial, and empirically supported to warrant full review rather than desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not detect hidden prompts, suspicious reviewer-directed instructions, or other manipulative content in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper studies interventional causal discovery in the presence of both latent confounders and post-treatment selection, arguing that standard interventional invariance-based formulations cannot distinguish true causal effects from selection-induced changes. The authors introduce a new equivalence notion, $\mathcal{FI}$-Markov equivalence, a new graphical representation called $\mathcal{F}$-PAG, and an algorithm $\mathcal{F}$-FCI that uses observational and interventional CI patterns to recover causal relations, latent confounding, and post-treatment selection up to this finer equivalence class. The paper also provides soundness/completeness claims and reports synthetic and gene-perturbation experiments.

## Strengths
The paper tackles a meaningful problem that is genuinely under-addressed in interventional causal discovery. The central observation, that post-treatment selection can mimic the same marginal-change/conditional-invariance pattern typically attributed to causation, is important and well motivated in Sections 1 and 2. The motivating examples in **Figure 1** are effective here: the pairs (a,b) and (c,d) make the identifiability failure concrete, and the paper correctly uses them to argue that existing PAG-style representations are too coarse for this setting.

A second strength is the attempt to go beyond merely pointing out the problem, the paper proposes a full framework: formalization via augmented DAGs with selection, a finer equivalence class, a new graph language, and an explicit recovery algorithm. This is more ambitious than a narrow empirical fix, and the scope is appropriate for a theory-oriented ICLR paper.

The graphical intuition is often strong. **Figure 4** is particularly useful because it links the proposed CI/invariance signals to concrete structural motifs. Even though some notation in the caption and surrounding text is sloppy, the figure helps the reader understand the intended distinction between asymmetric causal structures and symmetric selection-induced structures, and why interventions on auxiliary nodes such as $X_3$ may unlock finer discrimination.

The experimental section includes reasonably strong baselines for interventional causal discovery, including GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, and CDIS. The main synthetic comparison in **Figure 6** suggests that the proposed method is competitive and often better in precision/SHD, which is directionally consistent with the paper's claim that explicitly modeling post-treatment selection reduces spurious edges. The additional table on selection-identification accuracy, **Table 1**, is also useful because it evaluates a claim that is more specific than generic edge recovery.

The real-data application is relevant. Applying the method to single-cell perturbation data is a natural use case because quality-control filtering is exactly the kind of post-treatment selection mechanism the paper is trying to model.

## Weaknesses
1. **The formal definition of the target object is not yet clean enough, and this matters because the theoretical claims depend on it.**  
   The paper repeatedly claims to define a new equivalence notion, but **Definition 2 on Page 6** is underspecified in a way that makes it hard to verify the subsequent theorems. It says two augmented DAGs are $\mathcal{FI}$-Markov equivalent iff they have “the same d-separation ... among $X_{[N]\setminus\mathcal{I}}$” and “the same CI patterns between $\psi$ and any intervened variable.” This is not phrased at the same level of precision as standard Markov equivalence definitions. For example, it is unclear whether the CI patterns involving $\psi$ are meant over all conditioning sets, only endpoint conditioning, only those used by the algorithm, or some restricted family induced by intervention targets. This ambiguity is not cosmetic, because **Theorem 2** claims a necessary-and-sufficient graphical characterization of this equivalence class. If the equivalence relation itself is not crisp, the characterization becomes hard to assess. The paper needs a mathematically exact definition of the CI family being equated.

2. **Several mathematical statements are asserted at a high level, but the logical bridge between graphical separation and equality/inequality of distributions is too quick.**  
   In **Theorem 1 on Page 5**, the second and third bullets map d-separation relations involving $\psi$ to equalities or inequalities such as
   \[
   \psi_{I^{(k)}} \perp_d X_A \mid X_B \Rightarrow p^{(k)}(X_A\mid X_B)=p^{(0)}(X_A\mid X_B),
   \]
   and
   \[
   \psi_{I^{(k)}} \not\!\perp_d X_A \Rightarrow p^{(k)}(X_A)\neq p^{(0)}(X_A).
   \]
   The first implication is plausible under the augmented-DAG construction, but the second is much more delicate. Graphical dependence does not by itself guarantee inequality of distributions without additional faithfulness-style assumptions linking lack of separation to detectable distributional change. The theorem statement assumes positivity, but positivity alone is not enough for the “$\not\!\perp \Rightarrow \neq$” direction. Later the algorithm explicitly assumes faithfulness on **Page 8**, but **Theorem 1** itself does not state that assumption. This is a real issue because the theorem is used as the conceptual basis for the orientation rules.

3. **Equation (1) on Page 4 is not satisfactorily justified, and it mixes intervention semantics, conditioning on selection, and latent variables in a way that is easy to get wrong.**  
   The paper writes
   \[
   p_*^{(k)}(X)=\prod_{i\in I^{(k)}} p^{(k)}(X_i\mid \hat X_{pa_{\mathcal G}(i)},S=1)\prod_{j\notin I^{(k)}} p^{(0)}(X_j\mid \hat X_{pa_{\mathcal G}(j)},S=1).
   \]
   This looks like a modular factorization after intervention, but the factors are already conditioned on $S=1$, where $S$ is a descendant-type selection node depending on observed variables. Once one conditions on selection, the clean product factorization over local conditionals is not automatic in the usual SCM sense. The notation $\hat X_{pa_{\mathcal G}(i)} \subset X\cup L$ also hides whether latent variables are integrated out before or after conditioning on $S=1$. If this is intended as a conceptual shorthand rather than an actual factorization theorem, the paper should say so explicitly. As written, it reads like a formal probabilistic identity, and I am not convinced it is correct in general.

4. **Algorithm 1 is currently too underspecified and error-prone to support the “provably sound and complete algorithm” claim at the level of implementation detail expected from a main-track paper.**  
   The most obvious issue is in **Step 2.2 on Page 8**, where multiple different orientations are triggered by what appears to be the exact same CI pattern tuple, namely repeated lines of the form
   `if CI_s == (\perp, \perp, \perp, \perp) then Orient ...`
   yielding both $\leftrightarrow$ and $-$ in different lines. This cannot be correct as written. Either the tuples were mangled in typesetting, or the rule table is incomplete. In either case, the algorithm in the main paper is not self-contained enough to verify. Given that the contribution is algorithmic as much as conceptual, this is not a minor typo. The paper needs a precise rule table, preferably separated into exhaustive and mutually exclusive cases.

5. **The new graph language, $\mathcal{F}$-PAG, is intriguing but not yet presented with enough semantic precision to be comfortably usable.**  
   **Definition 5 on Page 7** introduces four mark types and many new edge types, but the textual explanation is too compressed. In particular, the semantics of the square mark $\square$ and the special edges used to denote inducing-path explanations are only informally described. The examples in **Figure 5** help a lot, especially the contrast between the DAG/MAG/PAG/$\mathcal{F}$-PAG rows, but even there the reader has to reverse engineer what is invariant versus what is only representationally convenient. If the point is that $\mathcal{F}$-PAG is a canonical graphical object for $\mathcal{FI}$-equivalence, the paper should specify exactly what each endpoint mark means in terms of ancestral/selection possibilities. Right now the representation is suggestive, but not yet fully operational.

6. **The soundness/completeness theorems are stated broadly in the main paper, but the proof presentation does not inspire enough confidence for claims of this generality.**  
   **Theorems 3 and 4 on Page 9** are central, yet the main-paper statements are high-level and the proof details in the appendix are uneven. For example, the proof sketch of **Theorem 3** relies on verbal arguments about unique CI signatures for tail, arrowhead, and square marks, but then introduces exceptions involving Y-structures and latent-confounding-plus-selection interactions, after which the guarantee seems to be qualified to some special path types. Likewise, the completeness theorem in the provided text is effectively truncated on **Page 19**, so from the main paper alone the justification is incomplete. Since the headline claim is “provably sound and complete,” the main text should be more precise about the scope, especially the dependence on Type I inducing nodes discussed later in Section 6.

7. **The empirical gains are real but not yet deeply analyzed, especially relative to the paper's strongest conceptual claim.**  
   **Figure 6 on Page 9** shows improvements over baselines, but the margins are not dramatic across all settings, and the figure aggregates over only 10 graphs. More importantly, the paper argues that its main advantage is distinguishing causation from post-treatment selection, yet the main figure reports generic DAG precision and SHD rather than a decomposition into errors due specifically to selection-induced confounding versus ordinary orientation mistakes. **Table 1 on Page 21** is a welcome addition because it directly measures selection identification, but the reported accuracy is only moderate in several settings, especially under soft interventions, for example around the mid-50s to mid-60s at smaller sample sizes. That does not invalidate the method, but it does suggest a more nuanced story than the prose in Section 5 currently conveys. The paper would be stronger if it clearly analyzed when the method helps most, for example as a function of number of selection nodes, intervention type, or availability of Type I inducing nodes.

8. **The real-data evaluation is interesting but weakly validated by the standards of causal discovery papers.**  
   The real-data section on **Page 10** is very short in the main paper and outsources the substantive discussion to the appendix. The evaluation appears to rely on external biological knowledge bases to support a subset of edges, but there is no quantitative comparison against baselines, no estimate of false positive rate, and no direct validation of the claimed post-treatment selection nodes. In a domain like gene regulation, cherry-pickable supportive evidence is easy to find. If the paper wants the biological case study to materially strengthen the paper, the main text should report a more systematic evaluation protocol.

9. **Exposition is rough in enough places that it slows down verification.**  
   There are multiple notation issues and likely typesetting errors, especially around separation symbols and CI statements in **Pages 3, 5, and 8**. For instance, some uses of $\sqcup_d$, $\nsubseteq_d$, and related symbols appear corrupted; the paper sometimes says “same skeleton and v-structure in the description of the corresponding MAG representation” where the exact graph object is unclear; and some sentences in the proofs are hard to parse grammatically. This is not just aesthetics. In a paper whose main contribution is a refined equivalence notion plus orientation logic, presentation quality directly affects assessability.

## Questions
1. In **Definition 2**, what is the exact family of CI statements that define $\mathcal{FI}$-Markov equivalence? Is it all CIs involving $\psi$ and observed variables over arbitrary conditioning sets, or only the specific endpoint/marginal/conditional patterns used by $\mathcal{F}$-FCI? A precise restatement would substantially increase my confidence.

2. Please clarify the assumptions behind **Theorem 1**, especially the step from graphical dependence to distributional inequality. Do you require faithfulness or some intervention-faithfulness condition? If yes, please make that explicit in the theorem statement rather than only in the algorithm section.

3. Is **Equation (1)** intended as an exact factorization identity after conditioning on $S=1$, or as an informal description of modular mechanism replacement under intervention? If exact, please justify why conditioning on the post-treatment selection variable preserves this product form.

4. Please provide the corrected and complete rule table for **Algorithm 1, Step 2.2**. As currently written, several distinct orientations appear to be triggered by identical CI tuples, which makes the algorithm impossible to verify from the main paper.

5. The paper emphasizes identifiability through Type I inducing nodes. How often are such nodes present in the simulation regime, and how sensitive are the results in **Figure 6** and **Table 1** to their prevalence? A stratified empirical analysis here could materially change my view of practical significance.

6. For the real-data experiment, can you provide a more systematic evaluation in the main paper, for example precision against a curated regulatory reference, comparison with at least one baseline, and a clearer operational definition of what counts as a detected post-treatment selection effect?

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No major ethics concerns stood out from the main paper. The biological application uses existing gene perturbation data and the paper does not propose harmful deployment scenarios.

## Soundness Rating
2: fair. The core idea is technically interesting and many claims are plausible, but key definitions, Equation (1), the exact assumptions behind Theorem 1, and the presentation of Algorithm 1 are not clean enough for a higher score.

## Presentation Rating
2: fair. The motivation and high-level story are good, and several figures, especially Figures 1, 4, and 5, help substantially. However, notation glitches, compressed definitions, and an error-prone algorithm description make the paper harder to verify than it should be.

## Contribution Rating
3: good. The paper addresses an important gap in interventional causal discovery and proposes a broader framework than a small incremental extension. Despite technical clarity issues, the problem formulation and the attempt to characterize a finer equivalence class are valuable to the community.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The paper tackles an important and relatively underexplored problem, and the overall framework is interesting enough that I can see value in acceptance. However, the current version has enough technical and expository roughness, especially around the formal definition of the equivalence class, Equation (1), and Algorithm 1, that my support is only cautious.

## Reviewer Confidence
4: confident. I am familiar with causal discovery with interventions, latent confounding, and PAG/FCI-style methods, and I checked the main technical claims carefully, though some ambiguities in the manuscript limit how far one can verify every detail from the main paper alone.