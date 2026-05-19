- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 3, 8, 8, 8
I'll proceed with writing the consolidated review based on my thorough verification of all claims against the paper.

---

## Summary

This paper proposes DSpodFL, a unified algorithmic framework for decentralized federated learning that jointly models sporadic SGDs (clients may skip gradient computations) and sporadic aggregations (communication links may be inactive) via arbitrary indicator random variables. This captures heterogeneous and time-varying computation/communication resources. The paper provides convergence analysis for strongly-convex and non-convex settings under constant and diminishing learning rates, showing geometric convergence to a neighborhood (convex) and sub-linear convergence (non-convex). It demonstrates that the analysis recovers known DGD, RG, and DFedAvg results as special cases, and reports 10–40% improved accuracy-delay tradeoffs in experiments on FMNIST/SVM and CIFAR10/VGG11.

## Strengths

1. **Unified framework subsuming multiple prior methods.** The paper models both sporadic SGDs and sporadic aggregations through arbitrary indicator variables $v_i^{(k)}$ and $\hat{v}_{ij}^{(k)}$. Section 3.2 and Figure 1 explicitly show that DGD, DFedAvg, and Randomized Gossip are special cases of DSpodFL for specific configurations of these indicators. Table 1 provides a systematic comparison showing DSpodFL satisfies all eight properties while each prior work covers only a subset. This unification is a genuine contribution.

2. **Convergence analysis with geometric rate and explicit optimality gap.** Theorem 1 (Eq. 14–15) proves geometric convergence $\mathcal{O}(\rho(\mathbf{\Phi})^{K})$ to a neighborhood for strongly-convex losses under a constant learning rate, with the optimality gap explicitly depending on $d_{\min}$ (minimum SGD probability) and $\tilde{\rho}$ (mixing spectral radius). The analysis recovers DGD guarantees when $d_{\min}=1$, demonstrating that the theory generalizes prior work. Proposition 1 provides an explicit sufficient condition on the learning rate for convergence.

3. **Milder assumptions than prior DFL work.** Assumption 3 only requires the asymptotic graph union to be connected with each edge appearing infinitely often (looser than static or $B$-connected assumptions). The data heterogeneity bound (Assumptions 1(c), 2(b)) uses two parameters $\delta$ and $\zeta$ where $\zeta$ can be nonzero, unlike works that force $\zeta=0$. The paper shows convergence bounds degrade gracefully with $\zeta$.

4. **Consistent experimental improvement across settings.** Across FMNIST (SVM) and CIFAR10 (VGG11), under both IID and non-IID data, DSpodFL achieves higher test accuracy at a given delay compared to DGD, RG, Sporadic SGDs, and DFedAvg (Figs. 3–4). The ablation study (Fig. 5) shows DSpodFL consistently outperforms baselines across varying label distributions, graph connectivity, network size, and resource heterogeneity levels.

## Weaknesses

### Fatal
None.

### Major

1. **Unspecified correlation structure for indicator variables undermines the generality of the convergence claims.** The paper assumes only that $v_i^{(k)}$, $\hat{v}_{ij}^{(k)}$, and $\epsilon_i^{(k)}$ are mutually uncorrelated (Assumption 2(b)). However, it does **not** specify whether $v_i^{(k)}$ and $\hat{v}_{ij}^{(k)}$ are independent of one another, independent across clients at the same iteration, independent across time, or — crucially — independent of the model parameters $\theta_i^{(k)}$. In Lemma 1, the bound uses $d_{\min}^{(k)} = \min_i \mathbb{E}[v_i^{(k)}]$, but applying this expectation requires factoring $v_i^{(k)}$ from functions of $\theta_i^{(k)}$. The paper states indicators "can vary arbitrarily over the training process according to decisions made by clients" (Sec. 3.2), which implies they could depend on model states. If a client skips SGD because its model is already good, $v_i^{(k)}$ and $\theta_i^{(k)}$ become correlated, and the expectation decompositions in the lemmas would need additional justification. **Why this matters:** this gap is structural — if the lemmas require independence conditions not stated, the convergence theorems may not hold under the claimed generality. The paper needs to either (a) state the required independence assumptions explicitly (and discuss any loss of generality), or (b) show the lemmas hold under the weaker uncorrelatedness condition alone (which would require a more involved proof).

### Minor

2. **The delay metric is internally consistent but not validated against real runtime.** The delay model $\tau_{total}^{(k)}$ is constructed from the same probabilities $d_i, b_{ij}$ that define DSpodFL's behavior (Sec. 5). While the metric is physically motivated (delay ∝ $1/d_i$ when computing, ∝ $1/b_{ij}$ when transmitting) and applied equally to all baselines, it is a synthetic proxy. The paper would benefit from at least one of: (i) a small-scale wall-clock time experiment on a testbed, (ii) sensitivity analysis showing robustness to alternative delay models (e.g., additive constant per operation), or (iii) a clear statement acknowledging this as a limitation. As written, the "training speed" claims rest entirely on this metric.

3. **Unspecified constants in the non-convex theorem.** Theorem 2 (non-convex) states the bound in terms of constants $w_1, \dots, w_5$ whose values and dependencies are not given in the main text (only "the values of scalars $w_1, \dots$" appears, with the definition cut off — likely deferred to the appendix, which is stripped by the parser). The main text should at minimum indicate what problem parameters each $w_i$ depends on; otherwise the theorem is uninformative without the appendix.

4. **Diminishing learning rate claim deferred to appendix without sketch.** The paper states (end of Sec. 4.3) that diminishing step size yields $\mathcal{O}(\ln K/\sqrt{K})$ convergence and a zero optimality gap, but provides no sketch or reference to a theorem number. For a claimed result that differentiates the paper from constant-step-size analysis, a brief roadmap or at least a theorem reference would help.

5. **Beta distribution choices for $d_i, b_{ij}$ are not fully justified.** The paper uses $\text{Beta}(0.5,0.5)$ for FMNIST and $\text{Beta}(0.8,0.8)$ for CIFAR10, with a brief motivation that $\alpha=\beta<1$ yields high heterogeneity. However, no rationale is given for choosing $0.5$ vs $0.8$, and sensitivity to these choices is only partially explored (Fig. 7(d) for the SVM/FMNIST case). The paper could be more transparent about why these specific values were selected.

### Trivial

6. **The betas for CIFAR10 (0.8, 0.8) are closer to uniform than (0.5, 0.5) for FMNIST**, but no explanation is offered for why a less heterogeneous setting was used for the more complex dataset. This is a minor clarity issue.

7. **The baseline DFedAvg period $D$ is set to $\lceil (1/m)\sum_i 1/d_i\rceil$ to match DSpodFL's average local steps**, but it is not stated whether DFedAvg was also tested with other $D$ values. A brief note would alleviate concerns that DFedAvg is disadvantaged by the choice.

## Nice-to-Haves

- A small table in the main text specializing the convergence bounds to DGD, RG, and DFedAvg with exact recovery of known rates would strengthen the "unification" claim without requiring readers to process the appendix.
- A non-trivial corollary showing how specific parameter settings for $d_i^{(k)}$ and $b_{ij}^{(k)}$ (e.g., based on resource availability measures) yield concrete convergence rates would demonstrate the framework's practical utility beyond recovering known special cases.
- Adding a brief remark on how to compute or bound $\tilde{\rho}^{(k)}$ in practice given random $\hat{v}_{ij}^{(k)}$ would help practitioners apply the sufficient condition in Proposition 1.

## Removed Points

- **"Last iterates claim is not a per-step guarantee"** — Removed because it is factually incorrect. Theorem 1 (Eq. 14) provides a bound on $\nu^{(K+1)}$, which is the error at the *last iterate*. It holds for every finite $K$, not just in the limit. The critic confused the limiting gap characterization (Eq. 16) with the main result.
- **"Matrix form requires stating symmetric communication assumption"** — Removed because the paper already explicitly states $\mathbf{P}^{(k)}$ is symmetric and doubly stochastic (Sec. 3.3) and defines $b_{ij}^{(k)} = b_{ji}^{(k)}$ (Definition 2).
- **"Typos in Lemma statements (parentheses)"** — Removed as formatting/parser artifacts per instructions.
- **"Public code release not mentioned"** — Removed per hard rule: questions about availability of external artifacts are not valid criticisms.
- **"Loose Graph Conn. novelty is marginal since Koloskova et al. 2020 also uses it"** — Removed because the paper's own Table 1 already credits Koloskova et al. 2020 with this property; the paper is transparent, not overclaiming.
- **"Results for CIFAR10 may need learning rate tuning"** — Removed as speculative; the same learning rate $\alpha=0.01$ is applied to all methods, which is a standard single-run evaluation practice.
- **Strength Finder: generic/superficial strengths** — Removed any that were sycophantic or generic (e.g., "this paper addresses an important problem" type claims not tied to specific evidence).
- **"DFedAvg may be disadvantaged by $D$ choice"** — Downgraded from weakness to minor clarity suggestion (now in Trivial #7) since the choice is explicitly motivated as matching average local steps.

## Novel Insights

None beyond the paper's own contributions. The two reviews do not surface a novel observation about the work that the authors themselves do not already articulate.

## Suggestions

1. **Clarify the correlation assumptions.** State explicitly in Section 4.1 whether $v_i^{(k)}$ and $\hat{v}_{ij}^{(k)}$ are assumed independent of each other, independent across time, and independent of the model parameters $\theta_i^{(k)}$ (conditioned on the history). If the proofs require independence (not just uncorrelatedness), say so and discuss the limitation. If the proofs work under weaker conditions, explain why.

2. **Add a real-runtime validation or acknowledge the synthetic delay limitation.** A small-scale wall-clock experiment (e.g., 2–3 clients on physical machines with controlled resource availability) would significantly strengthen the practical claims. Absent that, add a sentence to the limitations stating the delay metric is a proxy.

3. **Provide more context for the non-convex theorem.** Either state the dependence of $w_1,\dots,w_5$ on problem parameters in the main text, or provide a brief sketch of the structure of these constants.

4. **Justify the Beta distribution parameters.** Add a brief explanation for why $\text{Beta}(0.5,0.5)$ was chosen for FMNIST and $\text{Beta}(0.8,0.8)$ for CIFAR10.
