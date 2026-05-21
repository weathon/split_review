---
job_id: 7c0f0bc2-e94b-4181-9719-f5a4ad9a0160
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: Q6TymStAvS.pdf
paper: ShadowFM: Geometric Approaches for Learning Quantum Many-Body States with Flow Matching on Classical Shadows
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, it studies conditional generative modeling and flow matching on non-Euclidean geometries, with an application to quantum many-body systems.

## Minimum Quality
Pass ✅. The paper contains the expected scientific components, including abstract, introduction, method, experiments, quantitative results, related work, and conclusion. While there are important issues in technical clarity, mathematical specification, and empirical support, these do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or other suspicious content targeting automated review systems in the provided paper text.

# Expected Review Outcome:
## Summary
This paper proposes ShadowFM, a Hamiltonian-conditional generative framework for learning distributions of classical shadows of quantum many-body states using flow matching with geometric structure. The authors introduce two variants, a Riemannian spherical flow motivated by the Bloch sphere geometry of single-qubit shadows, and an anisotropic Dirichlet flow that encodes target versus anti-target pairing among Pauli outcomes, and evaluate them on TFIM and Heisenberg models using observable-estimation RMSE.

## Strengths
The paper tackles an interesting problem at the intersection of generative modeling and quantum many-body learning, namely learning Hamiltonian-conditioned distributions over classical shadows rather than directly over wavefunctions or observables. This is a reasonable and potentially useful formulation because shadows are already a compressed interface for downstream observable estimation.

The geometric motivation is intuitive and, at least at a high level, well aligned with the data structure. In particular, the argument in Section 3.1 that not all shadow errors are equally harmful is helpful. **Figure 2** is one of the stronger parts of the paper: it gives a concrete empirical motivation that spin flips are substantially more damaging than basis changes when reconstructing observables, which supports the authors’ claim that a geometry-aware model could be preferable to a geometry-agnostic one. Even if the full leap from this observation to the final methods is not completely nailed down, the motivating experiment itself is useful.

The paper covers multiple system classes and tasks. Beyond 1D TFIM and 1D Heisenberg ground states, it also includes a real-time dynamics extrapolation setup and a small 2D Heisenberg experiment. That breadth is better than many papers in this area, which often stay with a single toy Hamiltonian family.

There are some empirically promising results. In **Table 1** for TFIM with \(L=10\), both proposed methods substantially outperform the listed flow/diffusion baselines, and the anisotropic Dirichlet variant gets quite close to the oracle classical-shadow estimator at high inference budget for correlation RMSE. In **Table 3** and **Table 4**, the geometric methods also improve over LinearFM, Diff-LM, and StatisticalFM on Heisenberg correlation estimation. This suggests the methods are not merely overfit to a single benchmark.

The qualitative plots are also directionally supportive. **Figure 5(a,b)** suggests that the proposed methods track the sharp change around the TFIM phase transition more faithfully than LinearFM and StatisticalFM. **Figure 5(c)** also supports the claim that the proposed methods scale more favorably with training sample size than the non-geometric baselines, at least in the particular Heisenberg setting shown.

## Weaknesses
1. **The core geometric premise is only weakly connected to the actual shadow object being modeled, and the paper blurs the distinction between single-qubit measurement labels, local estimators, and full multi-qubit shadows.**  
   The main conceptual move is to interpret shadows through the Bloch sphere geometry, but the Bloch sphere corresponds to pure single-qubit states modulo phase, while the actual training data are discrete Pauli-6 measurement outcomes and, at the system level, tensor-product shadows across \(L\) qubits. The paper says on **Page 4**, “each single qubit state can be represented as a point on the three-dimensional unit ball ... This geometry is referred to as the Bloch Sphere,” but then the proposed generative model is used for shadow generation for many-body systems conditioned on Hamiltonians. The manuscript never clearly formalizes whether the model is generating per-site shadow tokens independently conditioned on context, a joint product-space manifold, or a full structured object with inter-site coupling in the state space itself. **Figure 1** visually suggests sequence-like generation of shadow strings with a transformer, while **Figure 3** reduces the geometry to a single \(S^2\). That mismatch matters because the claimed advantage is specifically geometric, but the paper does not establish that the chosen geometry is the right geometry for the joint object being learned.

2. **The mathematical formulation contains several notation and specification problems, including errors in the basic FM objective and inconsistencies in the training losses.**  
   In **Equation (1)**, the expectation is written as
   \[
   \mathbb{E}_{t \sim U[0,1], x_1 \sim q(\cdot), x_1 \sim p_t(\cdot \mid x_1)}[\cdots],
   \]
   which repeats \(x_1\) where the second sampled variable should clearly be \(x_t\). This may look minor, but it is exactly the core sampling procedure of conditional flow matching. Similar issues recur later. In **Equation (4)**, the loss is called \(\mathcal{L}_{\mathrm{CE},S^2}\), yet the text says “we optimize the Hamiltonian-conditional denoising classifier ... with cross entropy loss (equation 5),” even though the displayed equation is (4). Also, the expectation is written as
   \[
   x_0 \sim \pi_* p_\theta(\cdot),
   \]
   which is very odd because \(p_\theta\) is usually the learned model, not a fixed prior. From the surrounding text I suspect the authors intend a pushforward of a base distribution \(p_0\), but the equation as written does not say that. In **Equation (10)**, the expectation again samples \(x_1\) twice,
   \[
   x_1 \sim q(\cdot|\mathbf{e}), x_1 \sim p_t^{\text{AD}}(\cdot|x_1),
   \]
   where the second variable should be \(x_t\), and \(q(\cdot|\mathbf{e})\) is unexplained. These are not cosmetic issues, because they make the exact learning objective impossible to reconstruct unambiguously from the main paper.

3. **The derivation and validity of the anisotropic Dirichlet flow are under-explained in the main paper, and there are signs of internal inconsistency even before consulting the appendix.**  
   The method in Section 3.2.2 is the more custom and arguably more original part, but the main paper gives only the final expressions for \(C(x_i,t)\) and \(D(x_{\bar i},t)\) in **Equations (8) and (9)**, with essentially no derivation, no regularity discussion, and no explanation of numerical evaluation or stability. Since these coefficients involve singular-looking terms like \(x_i^{-\alpha_i(t)+1}\), \((1-x_i)^{-\alpha_\Sigma(t)+\alpha_i(t)}\), and integrands with \((1-s)^{-1}\), the paper should at least explain how these are evaluated robustly near the simplex boundary during inference. The appendix hints at a derivation, but the main paper still needs to define the actual computable object. More worrying, the text around **Equation (6)** says the path “tilts probability mass from the first vertex to the second as \(t\) grows,” which appears backwards or at least confusing relative to the intended target/anti-target interpretation. Also, **Equation (8)** integrates to \(x_{\bar i}\) rather than \(x_i\), which clashes with the fact that \(C\) is presented as a function of \(x_i\). Even if this is a typo, the method depends on these formulas, so the presentation in the main paper is not reliable enough.

4. **The Riemannian method is not fully convincing as a generative model over discrete shadows, and the bridge from classification to valid shadow sampling is underspecified.**  
   In Section 3.2.1, the model trains a classifier \(\hat p_\theta(x_1 \mid x_t,c)\) and then defines the marginal velocity field as a mixture of conditional velocities. This is standard in discrete flow matching variants, but here the state space is a sphere \(S^2\) with target points corresponding to a small set of discrete measurement outcomes. The paper does not explain how exactly the six Pauli outcomes map onto \(S^2\) in the training representation, whether antipodal points create ambiguities for the logarithmic map in **Equation (3)**, or whether the ODE trajectory can enter regions that do not correspond meaningfully to valid shadows before terminal decoding. **Figure 3** is helpful visually, but it actually exposes the concern: the model flows continuously on a sphere between sparse discrete landmarks. The paper never demonstrates that this continuous relaxation preserves the correct class probabilities better than simpler simplex-based embeddings, nor does it analyze pathological cases such as trajectories near antipodes where the sphere log map becomes delicate.

5. **The experimental evidence is promising but not yet strong enough to isolate the claimed source of improvement, especially the role of geometry.**  
   The empirical story is that respecting geometry helps, but the experiments mostly compare against fairly broad baseline families rather than cleanly controlled ablations. For example, the paper proposes two ingredients, spherical geometry and anisotropic target/anti-target probability paths, yet there is no controlled ablation separating:  
   (i) geometry-aware embedding only,  
   (ii) anisotropic path only,  
   (iii) same architecture with ordinary Dirichlet flow,  
   (iv) same architecture with Euclidean or simplex embedding but identical training budget.  
   Without such ablations, the gain could be due to architecture differences, better hyperparameter tuning, or the classifier parameterization rather than the advocated geometry itself. This is especially important because the headline claim is not merely “our model works better,” but “geometric consideration leads to more faithful sampling of shadows.”

6. **Several tables reveal a less consistent picture than the narrative suggests, and some results raise questions that the paper does not address.**  
   The strongest example is **Table 2** for TFIM with \(L=30\). There, for correlation RMSE, **Ours (Spherical)** is actually worse at 100k inference samples than at 10k, going from \(0.124 \pm 0.007\) to \(0.153 \pm 0.007\). That is not a trivial fluctuation, and it undermines the expectation that increasing \(M_{\mathrm{infer}}\) should reduce variance and expose the model’s asymptotic bias. If performance degrades with more generated shadows, that suggests a systematic mismatch in the learned distribution or an issue in the estimator pipeline. The paper does not comment on this anomaly. Likewise, in **Table 5** for real-time Heisenberg dynamics, **Ours (AD)** performs dramatically worse than Spherical on entropy RMSE, for example \(0.302 \pm 0.011\) vs \(0.179 \pm 0.003\) at 10k. This is an important failure mode for one of the two proposed methods, but the manuscript treats the result too casually. A paper arguing for a new family of geometry-driven flows should explain where and why one variant fails.

7. **The baseline set is incomplete relative to the paper’s claims and positioning.**  
   The introduction frames the contribution against autoregressive approaches and recent shadow generative models, but the experiments do not include a direct autoregressive shadow baseline, despite explicitly discussing sequential bottlenecks as motivation on **Pages 1–2**. If the claim is that a non-autoregressive method is preferable because it avoids sequential generation while maintaining or improving accuracy, then a direct empirical comparison is needed. The current baselines include kernels, LinearFM, Diff-LM, and StatisticalFM, but not the most obvious autoregressive conditional model over shadows. This omission weakens the practical case and makes the “non-autoregressive advantage” feel asserted rather than demonstrated.

8. **Important experimental details that affect validity are either missing from the main paper or buried in a way that makes the results hard to interpret.**  
   The main paper says for AD flow that \(\gamma \in \{0,0.05,0.1\}\) is evaluated and the best value is reported, but it does not state in the main text whether this selection is done per dataset, per observable, or globally, and whether the same criterion is used across all tables. Appendix D says model selection uses validation RMSE on correlation with \(M_{\mathrm{infer}}=10k\), which is better than tuning on test, but it also means entropy performance is not directly selected for. This matters because some of the entropy results, especially in **Table 5**, look unstable. Also, the reported datasets are relatively small, only 100 training Hamiltonians according to Appendix D, and the paper does not discuss sensitivity to this choice or whether conclusions persist across different random seeds for Hamiltonian families.

9. **The observable-estimation pipeline is itself not entirely cleanly described, and some formulas raise avoidable confusion.**  
   In Appendix A, **Equation (13)** for the \(Z_1Z_2\) estimator writes
   \[
   3(-1)^{b_1^{(k)}} \cdot 3(-1)^{b_1^{(k)}} = 9(-1)^{b_1^{(k)}+b_2^{(k)}},
   \]
   where the second factor should obviously depend on \(b_2^{(k)}\). I understand this is in the appendix, but it again contributes to a pattern: multiple equations at the level of core definitions contain mistakes that a careful pass should have caught. When a paper proposes new geometric flows and relies on nontrivial estimator pipelines, this level of sloppiness makes it harder to trust the exact implementation details behind the reported numbers.

10. **The paper’s claims are somewhat overstated relative to the evidence.**  
   The abstract claims that geometric consideration leads to “more faithful sampling of shadows” and “more accurate prediction of an unseen quantum state’s observables,” and the conclusion says the approach is the first to explicitly account for shadow geometry. The empirical evidence does support improved RMSE in many settings, but not uniformly across methods, observables, and tasks. Moreover, the paper never directly evaluates distributional fidelity of the generated shadows themselves, only downstream observable RMSE. Those are related but not identical claims. A more measured framing would say the proposed methods improve certain observable-estimation benchmarks under the reported setups, rather than broadly establishing faithful shadow sampling.

## Questions
1. Please clarify the exact training objectives in **Equations (1), (4), and (10)**. In each case, the sampled variables appear inconsistent, with \(x_1\) used where \(x_t\) seems intended. Could the authors provide the corrected equations and explicitly define all random variables and distributions? A precise statement of the training loss would significantly increase my confidence.

2. For the spherical method, what exactly is the state space for a full \(L\)-qubit shadow example? Is the model operating on a product manifold \((S^2)^L\), on per-site embeddings coupled by a transformer, or on some other relaxation? Please make this explicit in the main paper, not only in implementation details. Right now the geometric story is framed at the single-qubit level, while the learning problem is many-body.

3. In **Equation (3)**, how do you handle the antipodal or near-antipodal case for the sphere logarithmic map, where \(\sqrt{1-\langle p,q\rangle^2}\) becomes problematic? Since Pauli outcomes can correspond to opposite directions on the Bloch sphere, this is not a purely theoretical corner case. Please state whether any regularization or alternate branch choice is used in practice.

4. For the anisotropic Dirichlet flow, please clarify the apparent inconsistency in **Equation (8)**, where \(C(x_i,t)\) is defined through an integral with upper limit \(x_{\bar i}\). Is this a typo, or is there a cross-coordinate coupling intended? If it is a typo, please correct it and explain whether the experiments used the intended or printed formula.

5. Can the authors provide an ablation that isolates the source of the gain? In particular, I would like to see comparisons between standard Dirichlet flow, anisotropic Dirichlet flow with \(\gamma>0\), and the same classifier architecture without the geometric modifications. This would help determine whether the performance improvements really come from the proposed geometry rather than from model or tuning choices.

6. Please discuss the non-monotonic behavior in **Table 2**, where Spherical correlation RMSE gets worse from 10k to 100k inferred shadows, and the poor entropy behavior of AD in **Table 5**. These are important clues about model bias and failure modes. If there is a principled explanation, including it would strengthen the paper a lot.

7. Since the motivation explicitly contrasts your approach with autoregressive models, why is there no direct autoregressive baseline in the experiments? If such a baseline was tested but omitted for space, please report it in the rebuttal. If not, please justify why the non-autoregressive claim should be taken as sufficiently supported.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper presents a computational machine learning method for quantum many-body modeling and does not involve human subjects, personal data, or obvious deployment-sensitive applications. I do not see an ethics issue that requires dedicated review based on the content presented.

## Soundness Rating
2: fair. The main idea is plausible and some empirical gains are convincing, but the mathematical specification has multiple inconsistencies, the experimental evidence does not fully isolate the claimed mechanism, and several important anomalies are left unexplained.

## Presentation Rating
2: fair. The paper is readable at a high level and the figures help, but the exposition is undermined by repeated notation mistakes, ambiguous definitions, and an imprecise connection between the geometric story and the actual modeled object.

## Contribution Rating
2: fair. The problem is interesting and the geometric angle is potentially useful, but the current paper falls short of fully establishing that the proposed geometric modifications are the key reason for the gains, and the positioning against the most relevant alternatives is incomplete.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
I see a real idea here and the empirical results are better than trivial, but the paper in its current form is not tight enough for ICLR main track. The combination of objective-level notation errors, under-specified geometry, missing ablations, and unexplained result anomalies leaves me below the bar. A careful revision could improve this substantially.

## Reviewer Confidence
4: confident. I am confident in this assessment, though not absolutely certain. I am familiar with flow matching, geometric generative modeling, and the general quantum-ML context, and I checked the main equations and experimental claims carefully.