---
job_id: 24b3c4d8-e968-4038-b99a-23324b1df8c1
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 0zKfU1rsXd.pdf
paper: AQER: A Scalable and Efficient Data Loader for Digital Quantum Computers
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅ This paper is clearly within ICLR scope through optimization, learning-theoretic framing, and infrastructure/methodology for quantum machine learning and data loading.

## Minimum Quality
Pass ✅ The paper contains the necessary scientific components, including abstract, introduction, related work, methodology, experiments, results, and conclusion, and it presents a coherent technical contribution with nontrivial theory and empirical evaluation.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅ I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies approximate quantum loaders (AQLs), the problem of preparing target quantum states with limited circuit resources, and proposes a unified optimization view covering tensor-network-based and circuit-based approaches. The paper further presents an information-theoretic analysis relating achievable infidelity to a sum of single-qubit Rényi-2 entropies of the transformed target state, then uses this insight to design AQER, a heuristic loader that greedily reduces entanglement before a final refinement stage. Experiments on classical and quantum datasets, including MNIST, CIFAR-10, SST-2, random-circuit states, and TFIM ground states up to 50 qubits, show better infidelity-resource tradeoffs than the selected baselines.

## Strengths
The paper tackles an important bottleneck in quantum data processing. Efficient state preparation is a real pain point, and approximate loading is one of the few directions that has a chance of being relevant under realistic resource constraints.

The paper has a reasonably clear high-level conceptual contribution: it reframes several existing AQL methods under the common objective in **Equation (1)** and then uses an entanglement-based quantity to motivate a constructive algorithm. Even if the framework is not mathematically deep by itself, it gives a useful lens for comparing methods that otherwise look quite different.

The proposed AQER procedure is intuitively well structured. **Figure 2** is one of the strongest parts of the presentation, because it makes the three-stage design easy to follow: Step I reduces entanglement with two-qubit blocks, Step II builds a product-state approximation, and Step III refines the full circuit. This decomposition helps the reader understand what the method is actually doing, rather than hiding everything behind a black-box optimizer.

The empirical section is broad. The authors do not restrict themselves to one cherry-picked state family, but evaluate on classical data, synthetic quantum states, and many-body quantum states. This breadth matters here because the paper repeatedly claims generality across both classical and quantum inputs.

The quantitative results are consistently favorable to AQER on the selected benchmarks. In **Table 1**, AQER is best across all five datasets and all displayed gate budgets, often by a substantial margin. The strongest case is probably S-RQC: at \(G=40\), AQER reports \(0.128\) infidelity versus \(0.363\) for AQCE and \(0.484\) for HEC, and at \(G=80\), AQER reaches \(0.067\) versus \(0.267\) and \(0.367\). Even accounting for some mismatch in feasible gate counts across methods, the margin is large enough that this is hard to dismiss as noise.

The scaling plots are also supportive, at least empirically. **Figure 3(a)** does a good job connecting the theory to the observed behavior: across datasets, lower entanglement measure \(S\) tends to correspond to lower infidelity, and the points move down-left as \(T\) increases. This does not prove the theory is tight, but it does support the central design intuition of the algorithm. **Figure 4(b)** is also useful, since it suggests AQER does not immediately collapse as the qubit count increases on GS-TFIM.

The paper makes an effort to connect loading quality to downstream utility rather than only reporting fidelity. **Figure 5** is helpful in this respect: reconstructed images become visibly better as \(T\) increases, and the SST-2 classification error approaches the exact-loading baseline. For a state-preparation paper, this is a more convincing story than fidelity alone.

## Weaknesses
1. **The central theoretical claim is presented too strongly relative to what is actually established in the main paper.**  
   The paper repeatedly states, on **Pages 2, 5, and 10**, that infidelity is “fundamentally governed” or “controlled” by the entanglement measure \(S\), and even says reducing infidelity is “equivalent” to minimizing \(S\). That equivalence is too strong based on what is shown in the main text. **Theorem 3.1** gives lower and upper bounds on infidelity in terms of \(S\), but bounds do not imply that \(S\) is a sufficient surrogate objective for optimization, nor that two circuits with the same \(S\) will have similar infidelity. At best, the theorem shows \(S\) is informative and becomes linearly related in a small-\(S\) regime through Taylor expansion. This distinction matters because AQER is built entirely around the premise that minimizing \(S\) is a reliable proxy for minimizing the target loss. The empirical correlation in **Figure 3(a)** helps, but it does not justify the stronger “equivalent” language.

2. **The theorem statement and surrounding notation in the main paper are underspecified and inconsistent in ways that make the technical contribution harder to verify.**  
   In **Theorem 3.1** on **Page 5**, the upper-bound statement says “given access to \(\rho\), we can construct a product state \(|\psi'_{\mathrm{product}}\rangle\),” but \(\rho\) is not defined in the theorem statement. Presumably \(\rho\) is the density matrix of \(U^\dagger |\mathbf v_{\mathrm{target}}\rangle\), but the main text should not force the reader to infer this. Similarly, in **Equation (2)** on **Page 6**, the optimization is written as
   \[
   \mathcal I_t,\boldsymbol{\alpha}_t=\arg\min_{\mathcal I,\hat{\boldsymbol{\alpha}}}\mathcal S\left(V_{\hat{\mathcal I}}(\hat{\boldsymbol{\alpha}})\lvert\mathbf v_{t-1}\rangle\right),
   \]
   where the minimization variable is \(\mathcal I\) but the expression uses \(\hat{\mathcal I}\). This is a small notation bug, but in a paper that leans heavily on formalization, these details are not cosmetic. They directly affect whether the reader can check what is being optimized.

3. **The mathematical exposition contains at least one outright error in the preliminaries, which weakens confidence in the care taken elsewhere.**  
   On **Page 3**, the Pauli matrices are defined, but the matrix shown for \(Y\) is incorrect:
   \[
   Y=\begin{pmatrix}0 & -1\\ 0 & -1\end{pmatrix},
   \]
   whereas the Pauli-\(Y\) matrix should be
   \[
   Y=\begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}.
   \]
   This is not a deep flaw in the method, but it is not a harmless typo either. When a paper’s core contribution includes theorem statements, explicit gate formulas, and constructive parameter derivations, basic operator definitions need to be right. This sort of slip makes the reader more cautious about the rest of the derivations.

4. **The empirical comparison is promising, but the fairness of the baseline setup is not fully convincing from the main paper.**  
   **Table 1** compares AQER at \(G \in \{20,40,80\}\) against baselines that often use different gate counts, for example MPS at \(G=36,54,90\) on MNIST and AQCE at \(G=30,45,90\) on S-RQC. The authors say this is due to feasibility constraints and point to the appendix, but in the main paper this creates an awkward comparison: the headline claim is better accuracy and gate efficiency, yet the resource budgets are not uniformly matched. Since the entire paper is about efficiency tradeoffs, the comparison protocol should be crystal clear in the main text. It would be much stronger to show matched-budget interpolation or Pareto curves directly in the main paper rather than relying on a table with uneven \(G\).

5. **The claim about trainability and barren plateaus is overstated relative to the evidence provided in the main paper.**  
   On **Pages 2 and 6**, the authors suggest AQER mitigates vanishing gradients and barren plateaus. The main empirical evidence is **Figure 4(a)**, where the optimization curves for GS-TFIM with \(N=50\) decrease over training. That shows the procedure trains in that setting, but it does not establish absence or mitigation of barren plateaus in any meaningful general sense. To make that claim convincing, one would want explicit gradient-norm statistics across qubit number, random initializations, or comparisons to the HEC baseline under comparable conditions, none of which appear in the main paper. Right now the paper has evidence of optimization progress, not evidence of a mechanism-level explanation.

6. **The practical relevance to actual hardware remains underdeveloped in the main paper despite the title emphasizing digital quantum computers.**  
   The title and framing strongly suggest a loader for practical quantum devices, but all experiments in the main paper are numerical simulations. On **Page 6**, the authors mention that for quantum data, \(S\) and gradients are estimated from \(10^5\) simulated shots by default. This is not a small detail. A method can look excellent in state-vector or tensor-network simulation and still become unusable on hardware because of shot cost, noise, and calibration overhead. **Figure 3(c)** at least investigates shot count, which is useful, but there is still no main-paper evaluation under realistic gate noise or readout noise. For a paper that sells scalability and efficiency on digital quantum computers, this gap matters.

7. **The complexity and measurement overhead are not made sufficiently explicit in the main paper, which is a problem for an “efficient” loader paper.**  
   On **Page 6**, the paper says evaluating and optimizing \(\mathcal S\) is efficient because it only involves local measurements. That is directionally true, but incomplete. In Step I, the algorithm appears to search over qubit pairs and optimize a parameterized block at each iteration, which can become expensive even if each entropy term is local. The paper does not quantify in the main text how many candidate pairs are evaluated per iteration, how many tomography or measurement calls are needed per candidate, or how the total wall-clock or shot complexity compares to AQCE/HEC. **Figure 3(c)** gives only a partial view for GS-TFIM, and without the appendix the reader cannot assess whether the claimed efficiency is primarily in two-qubit gate count rather than total optimization cost.

8. **The downstream task evidence is suggestive but thin.**  
   The MNIST/CIFAR reconstructions in **Figure 5(a)** are visually intuitive, but they are qualitative examples only. The SST-2 experiment in **Figure 5(b)** reports classification error under a quantum kernel pipeline, yet the paper does not compare against the same pipeline using the baseline AQL methods. As a result, the downstream section mostly shows that improving AQER fidelity helps AQER’s own downstream behavior, which is unsurprising. It does not establish that AQER yields better downstream performance than alternative loaders under comparable budgets.

9. **Some writing choices drift into overclaiming.**  
   Examples include “consistently outperforms existing methods” and “paves the way for scalable quantum data processing and real-world quantum computing applications” in the abstract and conclusion. Given that the comparisons are against three baselines, mostly in simulation, with limited hardware realism and some uneven gate-budget matching, this rhetoric runs ahead of the evidence. The work is interesting, but the paper would benefit from a more disciplined statement of scope.

## Questions
1. In **Theorem 3.1**, please define \(\rho\) explicitly in the main text and clarify the exact construction assumptions behind the upper bound. Is the product state \(|\psi'_{\mathrm{product}}\rangle\) constructed from the single-qubit marginals of \(U^\dagger |\mathbf v_{\mathrm{target}}\rangle\)? A clean, self-contained theorem statement would increase my confidence considerably.

2. The paper repeatedly states that minimizing infidelity is “equivalent” to minimizing the entanglement measure \(S\). Can the authors tone this down or justify it more carefully? If the intended meaning is heuristic rather than exact, please say so explicitly. If stronger conditions are needed for equivalence, state them.

3. For **Table 1**, can the authors provide a clearer main-paper justification of the unmatched gate counts across methods? Ideally, a rebuttal should include either matched-budget comparisons or Pareto-style curves in the same resource units for all methods. This would strengthen the efficiency claim quite a bit.

4. Can the authors provide more direct evidence for the trainability claim beyond optimization curves in **Figure 4(a)**? For example, gradient norms at initialization as a function of \(N\), or a comparison against HEC under the same loss and parameter count, would be much more convincing than saying the curves “do not exhibit barren plateaus.”

5. In **Equation (2)**, is the intended optimization variable \(\hat{\mathcal I}\) or \(\mathcal I\)? Also, how exactly is the search over qubit pairs implemented in practice, exhaustive over all \(\binom{N}{2}\) pairs or with some pruning? This is relevant for understanding the real cost of Step I.

6. Since the title emphasizes digital quantum computers, can the authors comment more concretely on hardware viability? In particular, what is the expected shot and noise sensitivity of Step I and Step III, and under what noise regime would the main claims still hold?

7. Please correct the Pauli-\(Y\) matrix on **Page 3** and carefully proofread the notation around the theorem and algorithm. This is fixable, but it should be fixed.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None.

## Soundness Rating
3: good. The core idea is technically plausible and supported by broad experiments, but several theoretical statements are underspecified or overstated in the main paper, and some empirical claims, especially around trainability and practical efficiency, are not as fully supported as advertised.

## Presentation Rating
2: fair. The paper is generally readable and the figures are useful, especially **Figure 2**, **Figure 3**, and **Figure 5**, but there are avoidable notation issues, one clear mathematical error in the preliminaries, and some overclaiming in the exposition.

## Contribution Rating
3: good. The paper addresses an important problem, offers a useful entanglement-based lens for AQL, and presents a competitive method with strong benchmark results, though the contribution falls short of being airtight because of the theory-to-practice gap and the presentation issues.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected.  
I lean positive because the problem is important, the method is sensible, **Table 1** is strong, and the experimental breadth is better than average for this area. That said, the paper needs a more careful theoretical presentation, more disciplined claims around barren plateaus and efficiency, and cleaner baseline comparison protocol.

## Reviewer Confidence
4: confident. I am familiar with the approximate state-preparation / quantum ML literature and checked the main-paper technical claims carefully, though I did not independently verify every appendix proof in full detail.