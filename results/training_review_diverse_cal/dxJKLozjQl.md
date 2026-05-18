Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper formalizes the problem of **data distribution valuation** (as opposed to dataset valuation), where the goal is to compare the value of sampling distributions from limited sample datasets. Under a Huber mixture model of data heterogeneity, the authors propose an MMD-based valuation method, use the aggregate distribution across vendors as a reference (relaxing the need for a ground-truth reference), and provide theoretical guarantees for both pairwise distribution comparisons and incentive compatibility. Empirical results on classification and regression tasks demonstrate competitive ranking performance and empirical IC verification.

## Strengths

- **Formalizes a novel problem.** The paper clearly distinguishes data distribution valuation from dataset valuation and identifies why existing methods (Data Shapley, LAVA, DAVINZ, etc.) cannot answer whether one *distribution* is more valuable than another from samples. This framing is well-motivated by real data marketplace use cases.

- **Derives an interpretable closed-form valuation under the Huber model.** Eq. (2) — $\Upsilon(P) = -\varepsilon\, d(P^*, Q)$ — precisely captures how the outlier proportion $\varepsilon$ and the divergence $d(P^*,Q)$ affect distribution value. This is a clean, theoretically grounded result that prior work lacked.

- **Uses the aggregate distribution $P_N$ as a reference with explicit error bounds (Proposition 2, Theorem 1).** Replacing the unknown $P^*$ with $P_N$ is a practical contribution. Proposition 2 bounds the error by $\varepsilon_N d(Q_N, P^*)$, and Theorem 1 provides probabilistic guarantees for comparing distributions from samples using this proxy reference. The coupling of Huber convexity (Observation 1) with MMD's triangle inequality is technically elegant.

- **Empirically demonstrates strong ranking performance without a validation set.** In the challenging "without $D_{\text{val}}$" setting (Tables 1–4, right columns), Ours achieves the highest or near-highest Pearson correlations on multiple datasets (CIFAR10/CIFAR100, TON/UGR16, CaliH/KingH, Census15/Census17), outperforming baselines like IG, VV, and DAVINZ that degrade without a reference.

- **Empirically verifies IC for the tested mis-reporting direction.** Figures 1–2 consistently show a negative value change for the mis-reporting vendor under Ours, with a more pronounced drop than under MMD².

## Weaknesses

### Fatal
None.

### Major

- **One-sided IC definition with unsubstantiated "w.l.o.g." (Definition 1).** The paper restricts its IC analysis to mis-reporting that makes data *worse* relative to $P^*$ ($d(P,P^*) < d(\tilde{P},P^*)$), labeling this "w.l.o.g." with no justification. The alternative direction — a vendor reporting data *closer* to $P^*$ than their actual distribution (e.g., by surreptitiously including $P^*$ samples) — is a form of strategic mis-reporting that the IC guarantees do not cover. Corollary 1 confirms this: the exact-IC condition becomes harder to satisfy when $d(P_i,P^*) - d(\tilde{P}_i,P^*) > 0$ (i.e., the vendor "improves"). The "w.l.o.g." claim is not argued or supported, and the empirical IC evaluation (Section 6.2) only tests noise addition (the worsening direction). This does not invalidate the IC results for the worsening direction — which is the primary practical concern (vendors passing off low-quality data) — but the paper overclaims by not scoping this limitation. The abstract and introduction state the method "achieves incentive compatibility" without qualifying that this covers only one direction of mis-reporting.

  *Why this is major, not fatal*: The worsening direction is arguably the most relevant for data marketplaces (preventing vendors from reporting lower-quality data than they possess). The theoretical analysis for this direction is sound. However, the unqualified claim and unsubstantiated "w.l.o.g." need to be addressed before acceptance.

### Minor

- **Ground truth ranking estimation lacks transparency.** Section 6.1 defines $\zeta_i = \mathbb{E}_{D_i \sim P_i}[\text{Perf}(\mathbf{M}(D_i); D_{\text{test}})]$ and reports "average and standard error over 5 independent random trials," but does not specify how many inner draws from each $P_i$ are used to estimate each $\zeta_i$. If the number of draws is small, the "ground truth" itself is noisy, making the reported Pearson correlations less reliable. The procedure should be clarified.

- **The $n=1$ corner case is not discussed.** If there is only one vendor, $P_N = P_1$ and $\hat{\Upsilon}(P_1) = -d(P_1,P_1) = 0$, which is degenerate. The paper implicitly assumes $n \ge 2$ but never states this. A brief discussion would help.

- **No empirical investigation of differing vendor sample sizes.** The $\omega_i$ weights appear in Observation 1 and Corollary 1, but there is no experiment examining whether a vendor with a much larger sample dominates the reference and distorts valuations for others.

- **The Huber model limitation is acknowledged but the presentation could be sharper.** While the paper honestly states this limitation in Section 7, the title and abstract could more prominently qualify that the theoretical guarantees are Huber-specific. The critic's concern about readers over-generalizing is reasonable.

### Trivial
- The asymmetry of the factor 2 on the $1/\sqrt{m^*}$ term in $\Delta_{\Upsilon,\nu}$ (Proposition 1) could use a brief explanatory comment.

## Nice-to-Haves

- **Practical guidance for parameter selection.** Proposition 1 and Theorem 1 provide probabilistic guarantees with parameters $\varepsilon_{\text{bias}}$, $\varepsilon_\Upsilon$, $m$, $m'$, $m_N$ in a trade-off, but the paper does not offer concrete rules of thumb or example configurations. A brief algorithmic recipe or illustrative example would move this from "a policy exists" to "here is how to use it."

- **IC experiment with an "improving" mis-report.** Adding one experiment where a vendor surreptitiously includes data closer to $P^*$ (e.g., mixing in a small amount of $P^*$ data) and showing whether their value still decreases would directly address the IC scope concern.

- **Discussion of kernel choice sensitivity.** The MMD is defined by the kernel (RBF with a bandwidth parameter), but the paper does not analyze sensitivity to this choice. A brief experiment or reference to known robustness would strengthen the empirical claims.

- **Non-Huber experiment in the main paper.** The paper references non-Huber settings in the appendix; including one representative non-Huber result in the main body would reassure readers about robustness.

## Removed Points

- **"Typo in Proposition 1"** — The apparent formatting issue ($\Delta\Upsilon,\nu$ instead of $\Delta_{\Upsilon,\nu}$) is a parser artifact from PDF extraction, not an author error. Removed per hard rules on formatting artifacts.

- **"Ours cond. is not an instance of the proposed method"** — The paper explicitly presents Ours cond. as an extension ("We also extend our method..."), and notes it requires $D_{\text{val}}$. No misrepresentation. Removed.

- **"Comparison with MMD² nearly identical in ranking"** — This is not a weakness: similar ranking performance is expected since the values differ only by a square. The paper's advantage is theoretical IC, which it states. Removed as non-critical.

- **"Criterion margin additivity asymmetry"** — This is a minor technical observation about the factor 2 on the $m^*$ term. Moved to Trivial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a fundamentally novel perspective that the paper itself does not articulate.

## Suggestions

1. **Justify or remove the "w.l.o.g." in Definition 1.** Either provide a clear argument for why only the worsening direction is strategically relevant in your marketplace model, or broaden the IC definition and analysis to cover both directions. At minimum, explicitly qualify the scope of the IC claim in the abstract and introduction.

2. **Specify the ground truth estimation procedure** — state how many inner draws of $D_i \sim P_i$ are used to estimate each $\zeta_i$ in the ranking experiments.

3. **Add a brief discussion of the $n=1$ corner case** and clarify that the method assumes $n\ge 2$.

4. **Include one non-Huber experiment in the main paper** (even briefly) to demonstrate robustness beyond the theoretical premises.

## Score and Decision

This paper makes a solid and timely contribution: it identifies a genuine problem gap (distribution valuation, not dataset valuation), proposes a theoretically grounded method combining the Huber model with MMD, provides a clever solution for the missing-reference problem via the aggregate distribution with bounded error, and delivers practical empirical results. The theoretical analysis (Proposition 2, Theorem 1, Corollary 1) is technically sound and non-trivial.

The central weakness is the unqualified IC claim with a one-sided definition. However, this is addressable with clearer scoping and justification. No flaw invalidates the core contribution.

This is a solid paper suitable for acceptance after addressing the IC scope issue in revision.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>