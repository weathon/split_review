Now I have all the information needed. Let me synthesize the final review.

---

## Summary

This paper proposes MEHA (Moreau Envelope based Hessian-free Algorithm), a single-loop, Hessian-free gradient-based method for nonconvex-nonconvex bilevel optimization. The core idea is to reformulate the BLO using the Moreau envelope of the lower-level problem, which makes the proximal problem strongly convex even when the original LL problem is not, thereby enabling a single-loop scheme with non-asymptotic convergence guarantees under only smoothness and weak convexity — removing the PL condition or convexity required by prior work. Experiments on synthetic problems, few-shot learning, data hyper-cleaning, and neural architecture search show that MEHA achieves competitive accuracy with substantially lower runtime than existing BLO methods.

## Strengths

1. **Novel single-loop, Hessian-free algorithm via Moreau envelope reformulation**: MEHA is, to the best of my knowledge, the first algorithm to combine Moreau-envelope-based BLO reformulation with a single-loop scheme that avoids all Hessian computations. Table 1 clearly positions MEHA as the only method that is simultaneously Hessian-free, single-loop, and provides non-asymptotic convergence for the general nonconvex LL setting without PL condition or boundedness assumptions.

2. **First non-asymptotic convergence for general nonconvex-nonconvex BLO without PL condition**: Theorem 1 provides explicit rates ($O(K^{-(1-2p)/2})$ for stationarity, $O(K^{-p})$ for constraint violation) under only $L$-smoothness and weak convexity. This is a genuine relaxation of the PL/strong-convexity barrier that all comparable Hessian-free methods (BOME!, V-PBGD, GALET, SLM) require.

3. **Consistent and often dramatic runtime advantages across diverse tasks**: Across synthetic problems (Tables 2–4), MEHA is 30–98× faster than grid/random/TPE on high-dimensional nonsmooth problems. In few-shot learning and data hyper-cleaning (Table 6), it achieves the best accuracy/F1 while being the fastest — often by a wide margin (e.g., 130s vs 557s for RHG on 10-way). In NAS (Table 7), it reaches 96.07% test accuracy, the best among all methods compared.

4. **Relaxed assumptions clearly catalogued**: Table 1 provides a clean, honest enumeration of what each competing method requires. The smooth case of MEHA needs only $L$-smoothness of both objectives, while competing methods additionally need compactness, gradient-boundedness, or PL condition.

5. **Parameter sensitivity analysis**: Table 5 systematically varies five algorithm parameters and shows stability across a wide range, which is practically useful.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are supported by the theory and experiments; no verified weakness undermines the central contribution.

### Minor

1. **Framing could more precisely distinguish the relaxed problem from the original BLO**: The paper explicitly states (lines 241–253) that when the LL is nonconvex, the Moreau-envelope reformulation is equivalent to a relaxed problem where $y$ must be a *stationary point* of the LL (set $\tilde{S}(x)$) rather than a global minimizer (set $S(x)$). This disclosure is present. However, the abstract, introduction, and contributions section repeatedly refer to "general nonconvex Bi-Level Optimization" and "general BLO problems" without flagging this relaxation upfront. Readers unfamiliar with the literature could come away thinking the algorithm finds points satisfying the exact nested optimization, when it finds stationary points of a first-order relaxation. The authors should signal this distinction more prominently (e.g., "first-order stationary BLO" or "relaxed BLO") in the abstract and contributions.

2. **Theory-practice gap in convergence rates is not discussed**: Theorem 1 gives $\min R_k = O(K^{-(1-2p)/2})$. With $p=0.49$ (the "Original" setting in Table 5), the worst-case bound is $O(K^{-0.01})$ — essentially flat. Yet the algorithm converges rapidly in practice (97 steps). The remark (lines 423–425) notes that $p=0$ gives $O(1/\sqrt{K})$, but the discrepancy between the $p=0.49$ bound and empirical behavior is not addressed. Some discussion of when the bound is tight, or practical guidance for choosing $p$, would improve the paper. (Worst-case bounds are often loose, but ignoring the gap weakens the narrative.)

3. **Missing standard deviations in NAS experiments**: Table 7 reports test accuracy for NAS without standard deviations or confidence intervals. Other experiments (e.g., Table 6) include error bars. For a result like 96.07% vs 95.57% (DARTS), the difference is modest, and without variance information it is impossible to assess statistical significance.

4. **No code or repository provided**: No public code is mentioned, which hinders reproducibility and adoption. The paper would benefit from releasing an implementation.

5. **Missing justification for the weak convexity of Assumption 2(ii)/(iii)**: The paper claims (line 380) that cases (ii) ($x\|y\|_1$) and (iii) (group lasso) are instances of case (iv) (joint weak convexity + proximal Lipschitz condition). This claim is mathematically correct (e.g., $x\|y\|_1$ with $x\ge0$ is weakly convex with constants satisfying $\rho_{g_1}\rho_{g_2} \ge 1$), but the paper provides no proof or reference. Since the Lasso hyperparameter experiment (Eq. \ref{eq:LNS}) uses this case, a brief verification would strengthen confidence that the theory covers the experiments.

6. **Practical parameter selection guidelines are absent**: The sensitivity analysis shows robustness, but there is no practical guidance for choosing $\alpha, \beta, \eta, \gamma, \underline{c}, p$ in new applications. The theoretical ranges involve unknown constants (Lipschitz, weak-convexity). A simple heuristic (e.g., "set $p=0$, choose $\gamma$ moderate, tune $\alpha$ by grid search") would significantly improve utility.

### Trivial

- Table 1 uses $\XSolidBrush$ and $\CheckmarkBold$ unlabeled. The caption defines "Bounded" and "Gradient-Bounded" but not the symbols themselves, making the table slightly harder to parse at a glance.

## Nice-to-Haves

- An ablation comparing MEHA against a double-loop variant (e.g., BOME!) on the same problem, reporting wall-clock time to reach a given stationarity measure, would concretely demonstrate the advantage of the single-loop design.
- A discussion of how to set $\gamma$ relative to the weak-convexity constants in practice.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The problem being solved is a relaxation of BLO, not the original problem" as a fatal/structural criticism**: The paper explicitly acknowledges this relaxation (lines 241–253). It is standard in the nonconvex BLO literature to work with stationarity measures rather than global optimality (cf. value-function-based methods like BOME! also use relaxed constraints). The framing could be more precise (kept as Minor #1 above), but this is not a structural flaw and does not invalidate the contribution.

2. **"Assumption on nonsmooth component is problematic"** (the claim that $x\|y\|_1$ may not be weakly convex): The function $x\|y\|_1$ with $x\ge0$ is indeed $(\rho_1,\rho_2)$-weakly convex (e.g., $x|y| + \frac{\rho_1}{2}x^2 + \frac{\rho_2}{2}y^2$ is convex for $\rho_1\rho_2 \ge 1$). The reviewer's factual concern about the function not being weakly convex is incorrect. The valid sub-concern (no proof provided) is preserved as Minor #5.

3. **"No experiments on truly large-scale problems (deep ResNets, etc.)"**: The paper tests on NAS (CIFAR-10), data hyper-cleaning (MNIST/FashionMNIST), and synthetic problems up to 1000+ dimensions. These are standard benchmarks for BLO papers. Demanding experiments on large-scale deep learning is scope creep.

4. **"Connection to hypergradient (Theorem 2) requires strong convexity"**: The paper explicitly states this limitation (line 427–428) and positions Theorem 2 as an optional connection for a specific subclass. This is not a weakness; it is transparent scoping.

5. **"Notation is heavy"** and other formatting/style nitpicks.

6. **"Table 1 symbols not defined"**: The caption does define the terms (lines 33–37). The symbols $\XSolidBrush$ and $\CheckmarkBold$ are conventional and clearly interpretable in context.

## Novel Insights

None beyond the paper's own contributions. The reviews raise no genuinely novel observation that was not already in the paper.

## Suggestions

1. Add a sentence to the abstract clarifying that the method finds points satisfying a first-order (stationary) optimality condition of the lower-level problem when the LL is nonconvex.
2. Include standard deviations for the NAS results, or explain why they are omitted.
3. Add a brief paragraph discussing the theory-practice gap in rates and providing practical guidance for choosing $p$ (e.g., "a fixed penalty ($p=0$) with $O(1/\sqrt{K})$ rate suffices in many settings; the increasing penalty $p>0$ is primarily needed for asymptotic exactness of constraint satisfaction").
4. Provide a sketch or reference justifying that Assumption 2(ii) and (iii) satisfy the joint weak convexity in (iv).
5. Release code in a public repository.

## Score and Decision
MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>