Now I have all the information I need. Let me write the final consolidated review.

## Summary

This paper proposes feedback-weight matching, a method to enable fine-tuning of fully connected neural networks using Direct Feedback Alignment (DFA). The core idea is to decompose pre-trained weights into products of feedback matrices, then re-initialize the weights to match those products, thereby inducing strong weight alignment (WA) and gradient alignment (GA) during subsequent DFA fine-tuning. The paper provides theoretical analysis (propositions for linear networks, conjectures for nonlinear extensions) and experiments on image classification (CIFAR-100/SVHN/STL-10) and NLP tasks (GLUE with BERT-Tiny/Small), showing substantial improvements over standard DFA fine-tuning.

## Strengths

1. **First formal characterization of why DFA fails at fine-tuning.** Proposition 3.3 provides a clear theoretical argument: pre-trained weights obtained via back-propagation do not satisfy the strong weight alignment condition with random DFA feedback matrices. This is a genuine conceptual contribution that explains the empirical observation reported in prior work (Chu & Bacho, 2024).

2. **Large and consistent empirical gains across vision and NLP.** Feedback-weight matching achieves 7.97% higher accuracy on CIFAR-100→SVHN (82.67% vs. 74.70%) and improves Pearson correlation on STSB from 0.10 to 0.76 for BERT-Small (Tables 1, 2). The gains are systematic across architectures and tasks, not cherry-picked.

3. **Ablation study cleanly isolates the contribution of each component.** Table 3 shows that removing weight matching degrades accuracy from 83.16% to 79.77% (TinyImageNet→SVHN), while removing feedback matching causes only marginal drops (55.54%→55.03%). Removing weight decay causes a drop from 55.38% to 48.82% (CIFAR-100→CIFAR-10). This decomposition of the method into its parts is informative and supports the design.

4. **Demonstrates first successful DFA fine-tuning of Transformer (BERT) models.** DFA has been difficult to apply to Transformers even for from-scratch training; this paper shows it can fine-tune BERT-Tiny and BERT-Small on GLUE tasks with meaningful performance (e.g., 0.53 Matthews on CoLA vs. 0.06 for standard DFA). This extends DFA's applicability to a practically relevant architecture class.

## Weaknesses

### Major

1. **The decomposition procedure required by feedback matching is underspecified and its feasibility is not analyzed.** The paper requires decomposing each hidden-layer pre-trained weight as \( \bar{F}_l \bar{F}_{l-1}^\top = W_l^0 \) where \( \bar{F}_l \in \mathbb{R}^{n_l \times n_L} \) and \( \bar{F}_{l-1} \in \mathbb{R}^{n_{l-1} \times n_L} \) (Definition 3.4). The product \( \bar{F}_l \bar{F}_{l-1}^\top \) has rank at most \( n_L \) (the output dimension). For wide hidden layers (e.g., dimension 512 in BERT-Small) with small output dimensions (e.g., 2 for MRPC, 10 for CIFAR-10), this is a severe rank constraint. The paper never acknowledges this constraint, discusses when exact decomposition is possible, or specifies what approximation to use when it is not (e.g., SVD-based low-rank approximation). The claim in Section 3.2 that feedback matching "preserves the knowledge embedded in the pre-trained weights" is only literally true under exact decomposition; under approximation it requires qualification. This is a significant methodological gap. — *The paper states on line 90: "Equation (6) requires us to decompose the pre-trained weight ... into ..." but provides no algorithm, no rank analysis, and no error analysis for the approximate case.*

2. **Several theoretical claims rest on unsubstantiated probabilistic statements.** Lemma 4.1 asserts that quantities \( r_{1<l<L} \) and \( r_L \) are "non-negative with high probability," but no probability space, distribution, or concentration argument is specified or referenced. This phrase appears once (line 141) with zero supporting reasoning. Since Lemma 4.1 is used to derive the error-reduction bound in Proposition 4.1, the lack of any justification undermines the weight-decay synergy theory. — *Verification: line 141 is the only occurrence; no probabilistic argument follows.*

### Minor

3. **The theoretical analysis is confined to linear networks, with nonlinear extension left as unverified conjecture.** Propositions 3.3, 3.6, 3.8, Lemma 4.1, and Proposition 4.1 are stated for linear or two-layer nonlinear networks. The generalization to deeper nonlinear networks is deferred to Conjectures 3.9 and 4.2, which are not empirically validated on the actual networks tested. For example, Conjecture 4.2's error bound (Equation 15) is never empirically checked. While linear analysis followed by nonlinear conjecture is a common paradigm and Figure 1 does empirically confirm WA/GA trends, the gap between the proven theory and the claimed mechanism remains wider than the paper acknowledges. — *Figure 1 shows WA and GA curves for the actual nonlinear networks, partially addressing Conjecture 3.9, but the specific error-bound prediction of Conjecture 4.2 is not validated.*

4. **Weight matching re-initializes the pre-trained weights, meaning the original pre-trained initialization is discarded.** The procedure sets \( \bar{W}_l^0 \equiv \bar{F}_l \bar{F}_{l-1}^\top \) (Equation 7). If the decomposition is inexact (which the rank constraint above shows it must be for wide layers), \( \bar{W}_l^0 \neq W_l^0 \), and the pre-trained knowledge is only approximately preserved. The paper does not measure the approximation error or its effect on downstream performance. The empirical results show the method works despite this, but the framing that "knowledge is preserved" (line 110) is overstated.

5. **The paper does not discuss whether the resulting algorithm retains DFA's claimed benefits (parallel updates, biological plausibility).** The feedback matrices are constructed from pre-trained weights rather than random, which departs from the biological motivation of DFA. The method is still backpropagation-free and supports parallel layer updates (since DFA's update formula still applies), but this is not discussed. A brief clarification would address the concern.

### Trivial

- The phrase "with high probability" in Lemma 4.1 should either be justified or replaced with a deterministic claim or an explicit assumption.
- The paper would benefit from specifying the hidden layer widths used in the image classification experiments, to allow readers to assess the rank constraint.

## Nice-to-Haves

- Empirical verification of the error bound in Conjecture 4.2 (e.g., plotting \( \|e^{t+1}\| \) against the RHS of Equation 15) would significantly strengthen the weight-decay synergy claim.
- Measuring per-layer (rather than aggregate) WA and GA would provide finer-grained support for the theory.
- A brief discussion of how the decomposition handles layers where \( \text{rank}(W_l^0) > n_L \) (e.g., using truncated SVD) and how approximation error propagates.

## Removed Points

These points were flagged by the harsh critic but are removed after verification against the paper:

1. *"The paper does not measure whether strong WA actually leads to strong GA in the non-linear networks tested"* — **Removed (factually wrong).** Figure 1 explicitly plots WA and GA for the actual nonlinear networks used in fine-tuning (both image and BERT models). The paper does measure this relationship.

2. *"No proofs or even proof sketches are given in the main text... clearly state that proofs are in a non-stripped appendix"* — **Removed (parser artifact).** The parser strips appendix content from all papers. The original submission almost certainly contains proofs in the appendix.

3. *"BERT-Tiny and Small are far from modern foundation models"* — **Removed (scope creep).** This is a proof-of-concept for DFA fine-tuning; demanding BERT-Base/Large experiments would constitute a substantially different paper. The paper's contribution does not depend on scaling to 340M-parameter models.

4. *"The method deviates from DFA's core property of using random feedback... questions what is actually being contributed"* — **Removed (evaluates against wrong class of expectations).** The paper proposes a *fine-tuning* method, not a biology-plausibility paper. The method remains backpropagation-free and supports parallel updates. The departure from random feedback is the *point* of the method (feedback matching is a design choice, not an oversight).

## Novel Insights

The most interesting insight that emerges from synthesizing the reviews is deeper than what the paper itself states: feedback-weight matching can be understood as a form of **weight-space alignment via explicit low-rank factorization** that converts a back-propagation-trained initialization into one that lies in the natural "basin of attraction" of the DFA dynamics. Standard DFA fails at fine-tuning because the pre-trained weights sit outside the manifold of matrices that satisfy strong weight alignment with any set of random feedback matrices. By constructing feedback matrices from the pre-trained weights and then re-initializing to match, the method effectively projects the initialization onto the DFA-compatible manifold. The rank constraint (\( \text{rank} \leq n_L \)) is therefore not just a technical detail but a fundamental limitation: the projection inherently loses any pre-trained knowledge that resides in the rank-\(> n_L\) subspace. This suggests the method's headroom is bounded by how much task-relevant information the top-\(n_L\) singular components of the pre-trained weights carry — an empirical question the paper does not investigate but which would be fascinating future work.

## Suggestions

1. **Specify the decomposition algorithm** — describe exactly how \( \bar{F}_l \) and \( \bar{F}_{l-1} \) are computed from \( W_l^0 \) (e.g., via SVD with truncation to rank \( n_L \)), and analyze the rank constraint explicitly.

2. **Justify or replace the "with high probability" claim** in Lemma 4.1 — either provide a concentration argument or state the lemma under explicit assumptions that guarantee non-negativity deterministically.

3. **Measure the decomposition error** \( \| \bar{F}_l \bar{F}_{l-1}^\top - W_l^0 \| \) for each layer and discuss how it correlates with final fine-tuning performance.

## Score and Decision

This paper tackles a real problem (DFA cannot fine-tune), proposes a clever solution (feedback-weight matching), and delivers strong empirical results. The core idea is novel and the experiments are reasonably thorough across two domains. However, the paper contains a significant methodological gap: the decomposition procedure at the heart of the method is underspecified, its mathematical feasibility is not analyzed, and a key theoretical claim ("with high probability") lacks any supporting argument. These are addressable in revision but make the current version incomplete. The contribution is worthwhile, but the paper needs another round of development.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>