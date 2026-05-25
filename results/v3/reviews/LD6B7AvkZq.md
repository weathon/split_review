Now I have sufficient anchor data to make a well-calibrated assessment. Let me write the full consolidated review.

---

## Summary

This paper studies how small transformers learn probabilistic context-free grammars (PCFGs) by introducing a formal notion of "subgrammar" (inner and outer). It claims a set of theorems decomposing the language‑modeling KL divergence into a sum over subgrammars, and presents experiments on parallel subgrammar learning, curriculum pretraining on subgrammars, and depth‑vs‑length generalization. The core idea — that grammar substructure can be formalized and linked to learning dynamics — is genuinely novel, but the execution has significant shortcomings that prevent the paper from meeting a high bar.

## Strengths

1. **Novel formalization of subgrammar structure.** Definitions 3.3 (inner subgrammar) and 3.5 (outer subgrammar) provide a precise, novel framework for decomposing CFGs into meaningful substructures. This formalization is well‑motivated and is a genuinely new contribution to the study of how neural networks acquire hierarchical syntax.

2. **Empirical demonstration that total KL decomposes into subgrammar components.** Figure 1 shows that throughout training, the measured subgrammar‑level KL divergences sum to the total loss, providing empirical evidence consistent with the claimed decomposition. The visual clarity of this result is compelling.

3. **CKA analysis with 30 random seeds.** Table 1 reports cross‑seed Centered Kernel Alignment for attention and MLP layers under several conditions. The finding that 20‑epoch pretraining increases attention‑layer CKA by +21.7% (full grammar) and +20.8% (subgrammar sequences) on 2‑layer transformers, relative to training from scratch, is the most quantitatively solid result in the paper.

4. **Transparent acknowledgment of limitations.** The paper notes that the curriculum benefit disappears for 4‑layer models, that the GPT‑5.1 test is purely anecdotal, and that the context‑insensitivity assumption is strong. This candor is appreciated.

## Weaknesses

### Major

1. **The core theoretical derivation is not clearly presented and cannot be verified from the main text.** The derivation in Section 4.2 (equations 1–4) contains mathematical notation that does not follow from standard KL manipulations. Equation (4) presents log‑ratios where the numerator and denominator are both log probabilities (i.e., `log P / log Q`), which is not a standard KL expression and appears to be a formatting corruption of the intended derivation. Definition 4.2 (restricted KL) uses unclear notation (`D_KL(P_G ∥ Q | ¬s)` is not a standard conditional KL) and is not self‑explanatory. Since the paper advertises the loss‑decomposition theorems as "the most important contribution," this lack of clarity in the main text is a significant weakness. The proofs are relegated to Appendix A, which is not accessible to us, so the correctness of the claimed theorems cannot be independently assessed. **Why it matters:** A reader cannot judge whether the central theoretical claim is valid from the material presented in the main body.

2. **The "parallel learning" claim is not rigorously demonstrated.** The observation that subgrammar losses decrease simultaneously (Figures 1–2) is consistent with the total loss decreasing and is largely a consequence of the claimed decomposition (Theorem 4.3) rather than an independent empirical finding about learning dynamics. No baseline (e.g., a staged training regime where subgrammars are introduced sequentially) is provided to establish what non‑parallel learning would look like. The contrast with child language acquisition is rhetorical — no developmental data are used. Corollary 4.7 states a sufficient condition (gradient independence) that is essentially definitional and is not tested. **Why it matters:** One of the paper's main empirical claims rests on an observation that is weaker than the paper's framing suggests.

3. **Overclaiming relative to what is actually shown.** The paper describes the theoretical results as "fundamental theorems" and claims that the CKA analysis "show[s] definitively" that pretraining aligns representations with grammar substructure. The CKA increases are modest (+8.9% to +21.7% on attention layers; most MLP changes are near zero or negative), and the theoretical derivation is not independently verifiable from the text. This mismatch between rhetorical strength and evidential support weakens the paper's credibility. **Why it matters:** The paper's impact is diminished when readers cannot trust the strength of the claims relative to the evidence.

### Minor

4. **Curriculum learning benefit is limited and potentially a small‑model artifact.** The benefit of subgrammar pretraining on final loss (Figure 6, referenced but not in the visible text) only holds for 2‑layer transformers and disappears for 4‑layer models. The paper acknowledges this, but the finding's generality is therefore narrow. The pretraining benefit on CKA is similarly concentrated in attention layers with modest effect sizes.

5. **The depth‑vs‑length experiment (Section 6) replicates known findings.** The result that transformers struggle with deep recursion but not with long non‑recursive strings has been documented before (the paper cites Lampinen 2024). The GPT‑5.1 test is explicitly anecdotal and adds no rigorous evidence. This section does not advance beyond what is already known about transformers and recursive structure.

6. **Theorem 4.6 (KL divergence with expected recursion) states a relatively straightforward observation.** The result that expected recursion ≥ 1 makes KL unbounded follows from the PCFG not defining a proper normalized distribution, and is a basic consistency condition rather than a substantive theorem about learning dynamics.

7. **The context‑insensitivity assumption (Corollary 4.5) is acknowledged as strong but not tested.** The paper mentions that experiments "suggest" the condition may hold statistically, but no quantitative test is provided. This limits the applicability of the simplified decomposition.

### Trivial

- Figure 6 is referenced in the main text but does not appear in the visible body of the paper.

## Nice-to-Haves

- A comparison of the observed learning dynamics to explicit predictions from the recurrence (e.g., does the rate of decrease for each subgrammar KL follow from the decomposition?).
- An analysis of whether inner or outer subgrammars are systematically easier to learn, which the decomposition might predict.
- A discussion of conditions under which parallel learning might fail (e.g., when subgrammars have very different statistical properties or when the model is not over‑parameterized).

## Removed Points

The following points from the inputs were removed after verification against the paper:

1. **"The step from lines (2)–(3) to (4) does not follow from any standard manipulation"** — Retained in weakened form as Major weakness #1. The original framing as "mathematically incoherent" is accurate in describing the presented equations, but some of the garbling may be a PDF formatting artifact rather than an error in the underlying mathematics.
2. **"No comparison of learning dynamics to theoretical prediction"** — Moved to Nice-to-Haves. This is a reasonable request but not a core flaw; the paper does not claim to provide such a comparison.
3. **"No connection to behavioral data from children"** — Removed. The child-language contrast is a motivating observation, not an empirical claim requiring full developmental data.
4. **"Hyperparameters relegated to appendix"** — Removed as a formatting nitpick. This is standard practice for conference papers.
5. **"Anecdotal GPT‑5.1 test does not belong in a research paper"** — The paper itself calls it "purely anecdotal" and includes a caveat footnote. Retaining this as a weakness would be penalizing transparency. It is mentioned tangentially in Minor weakness #5.
6. **"Missing related works"** — Removed per instructions. I cannot independently verify the existence of unmentioned works.
7. **"CKA changes are small and overlap with likely variance"** — The paper reports using 30 seeds and shows consistent patterns (e.g., +21.7% is a clear signal even if modest). The concern is addressed by noting the modest effect size in Major weakness #3, not by claiming the results are invalid.
8. **Strength Finder claims that depend on unverifiable theoretical content** — The Strength Finder's praise of the "recursive decomposition" as a proven theorem is downgraded since the derivation in the main text is not clear. The core idea is novel (retained as Strength #1) but the proof is not verifiable from the material provided.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no genuinely novel observation not already present in the paper's conceptual framework.

## Suggestions

1. **Rework the theoretical section** with a clean, step‑by‑step derivation. Start from the chain rule for KL divergence, define the restricted KL precisely (not with the garbled ¬s notation), and show each algebraic step. This is essential because the theory is advertised as the paper's main contribution.
2. **Rigorously benchmark the parallel‑learning claim.** Design an explicit baseline: train on subgrammars sequentially (e.g., freeze parameters after mastering one subgrammar, then train on the next) and compare convergence rates. Without this, "parallel learning" is just the observation that loss decreases.
3. **Calibrate the language.** Remove "definitively," "fundamental theorems," and "the most important contribution" unless the theory is presented with full rigor and the evidence is much stronger.
4. **Quantify the context‑insensitivity assumption.** Compute the variance of Q_θ's subgrammar predictions across different contexts and report it alongside the decomposition results. This would strengthen Corollary 4.5's applicability.
5. **Move the CKA absolute values to the main text** (they are the most quantitative evidence for representation alignment). Provide confidence intervals or standard deviations alongside the averages.

## Score and Decision

**Round‑1 bracket:** 3.0–5.0. Low‑band anchors (score < 3.5) failed at unclear/unsupported claims, overclaiming, and modest experiments on synthetic data — failures shared in part by this paper. Topic‑mid anchors (e.g., F0Zd3knG9j at 5.0) had cleaner execution but more novelty concerns; this paper is weaker along both dimensions (unclear theory, less rigorous experiments). Weakness‑anchored queries confirmed that papers with unclear theoretical derivations and unsupported central claims consistently score 2–4.

**Round‑2 narrowing:** Anchors within (2.5, 4.5) confirmed the bracket. The most topically similar anchor, hFQZmKFtlT (3.5, Reject) — training LLMs on PCFG data — shares the limitations of synthetic data and overclaiming. This paper has a stronger conceptual contribution (subgrammar framework) but worse execution on its advertised theoretical core. A score of 3.5 reflects this tradeoff: genuine novelty in the framework, undercut by a theoretical presentation that cannot be followed from the main text and experiments that do not fully support the strong claims.

**What the low‑band anchors failed at and does this paper share those failures?** The low‑band anchors (3.0–3.5) failed at: unclear contributions relative to the claims made, insufficient experimental rigor to support the stated conclusions, and overreliance on small synthetic experiments without proper baselines. This paper shares all three failures: the theoretical derivation is unclear, the parallel‑learning claim lacks a baseline, the CKA evidence is modest relative to the "definitively" language, and the depth experiment adds little to known results. The subgrammar framework is a genuinely novel contribution that the low‑band anchors lacked, which is why the score sits at 3.5 rather than 3.0. But the novelty does not compensate for the severity of the communication and rigor problems in the advertised core contribution.

ALL ANCHORS RETRIEVED:
- hFQZmKFtlT (3.5, Reject) — round1-weakness-curriculum / round2 — Training LLMs on PCFGs, similar topic. Closest topical comparator; our paper has stronger theoretical framing but similar execution quality.
- F0Zd3knG9j (5.0, Reject) — round1-topic-mid — Transformers on tree-structured data. Cleaner experiments but novelty concerns. Our paper is weaker.
- 0pLCDJVVRD (7.0, Accept) — round1-topic-mid — Formal language emergence. Stronger paper overall, accepted.
- fp77Ln5Hcc (4.5, Reject) — round1-topic-mid / round1-weakness-recursive-depth — Depth extrapolation of decoders. Comparable depth experiments; our paper is slightly weaker.
- MO5PiKHELW (5.5, Accept) — round1-weakness-curriculum — Syntax acquisition in MLMs. More thorough experimental design. Our paper is weaker.
- uOnElfFuey (3.0, Reject) — round1-topic-low — DFA extraction from LMs. Lower quality than our paper.
- eRkNNQRppH (3.5, Reject) — round1-weakness-curriculum / round2 — Pretraining dynamics with first-order logic. Comparable quality.
- STUGfUz8ob (7.6, Accept) — round1-topic-high — Abstract symbol reasoning. Much stronger paper.
- NSBP7HzA5Z (3.0, Reject) — round1-topic-low / round2 — Inductive transformers. Lower quality.
- sprjE7BTZR (3.75, Reject) — round2 — Transformers as compilers. Comparable quality.
- B6B6EhC1bW (2.5, Reject) — round1-topic-low — Molecular substructure. Lower quality.
- FwjEZZ3j91 (3.0, Reject) — round1-topic-low — Symbolic regression. Lower quality.
- 9PYCz4cDuZ (4.0, Reject) — round1-weakness-KL — Bias/diversity in MBR decoding. Different topic.
- z3DMFpaP6m (3.0, Reject) — round1-weakness-KL — Entropy of LMs. Different topic.
- o2uHg0Skil (6.25, Reject) — round1-weakness-KL — KL regularization in RL. Different topic.
- qyU5s4fzLg (7.5, Accept) — round1-weakness-curriculum — Unsupervised constituency parsing. Different topic.
- zDze7VtB5C (5.5, Reject) — round1-weakness-recursive-depth — Log-depth transformers. Different focus.
- b5lXUwZiD3 (5.25, Reject) — round1-weakness-recursive-depth — Transformers learning HMMs. Different topic.
- X65IKSuWQo (4.0, Reject) — round1-weakness-garbled — Diffusion models. Different topic.
- a8XwgTZzE0 (2.0, Reject) — round1-weakness-garbled — Grokking dynamical systems. Lower quality.
- OXIIFZqiiN (1.5, Reject) — round1-weakness-garbled — Patch analysis. Lower quality.

MY FINAL SCORE: <score>3.5</score>
MY FINAL DECISION: <decision>Reject</decision>