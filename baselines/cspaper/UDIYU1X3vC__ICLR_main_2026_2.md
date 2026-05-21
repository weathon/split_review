---
job_id: ee78204f-a46a-44e8-99b3-56dca39f858f
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: UDIYU1X3vC.pdf
paper: Proper Velocity Neural Networks
main_score_norm: 0.6
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, specifically representation learning on non-Euclidean geometries, hyperbolic neural networks, and applications to vision, graphs, and biology.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, presents a technically coherent method with derivations, and includes empirical evaluation across multiple tasks. While I have substantive concerns about novelty, experimental framing, and some mathematical exposition, these do not rise to the level of a desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find any hidden prompts, suspicious instructions to automated reviewers, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies the Proper Velocity (PV) model as an unconstrained representation of hyperbolic space and proposes Proper Velocity Neural Networks (PVNNs). The paper derives a Riemannian toolkit for PV space, including isometries to the Poincaré ball, exponential and logarithmic maps, parallel transport, and geodesic distance, then builds PV counterparts of MLR, fully connected, convolution, activation, and batch-normalization layers. The empirical section evaluates numerical stability and downstream performance on image classification, graph node classification, and genomic sequence learning.

## Strengths
The paper has a clear and fairly coherent technical arc. Sections 4 and 5 build from the PV-Poincaré isometry in **Theorem 4.2** to explicit operators in **Theorem 4.3**, and then to concrete neural layers such as PV MLR in **Theorem 5.2** and PV FC in **Theorem 5.3**. Even if one is skeptical about how much of this is fundamentally new versus transported from existing hyperbolic models, the paper does provide a reasonably complete intrinsic toolbox for working in PV coordinates.

I appreciated that the paper does not stop at abstract geometry. It goes all the way to implementable layer definitions, and the simplification from the geometric MLR in **Eq. (18)** to the matrix-multiplication-friendly form in **Eq. (19)** is practically meaningful. This is one of the better-motivated parts of the method section, because the authors actually explain why the naive formulation would materialize a \(b \times C \times n\) tensor and why the reparameterized form is computationally preferable.

The numerical stability section is useful. In particular, **Table 1** and **Table 2** support the main motivation that an unconstrained model can be easier to handle numerically than constrained hyperbolic models. The contrast is especially stark in **Table 2**, where the PV round-trip error for \(\|\mathrm{Log}_0(\mathrm{Exp}_0(v)) - v\|\) is substantially lower than both the Poincaré and hyperboloid counterparts in FP32, and much lower than hyperboloid even in FP64. This does not prove broad training robustness on its own, but it does support the narrower claim that the coordinate system is numerically benign for these basic operators.

The empirical evaluation is broader than many geometry papers. The authors cover not just one benchmark family but four settings, and that breadth helps establish that the proposal is not tied to a single task. **Table 10** is particularly encouraging in that PVCNN improves over both Euclidean CNN and HCNN-S on all listed genomic tasks, with visibly large gains on SINEs and unprocessed pseudogenes.

The paper is generally readable for a geometry-heavy submission. The progression from **Eq. (4)** to **Theorem 4.3**, then to **Eq. (19)** and **Eq. (22)**, is understandable, and the Euclidean limit discussions after **Theorem 5.2** and **Theorem 5.3** help sanity-check the constructions.

## Weaknesses
1. **The main conceptual novelty is narrower than the paper sometimes suggests, because most of the machinery is inherited through isometry from existing hyperbolic models.**  
   This is the central issue for me. The paper explicitly proves in **Theorem 4.2** that PV and the Poincaré ball are Riemannian isometric, and Appendix D further shows a direct isometric connection to the hyperboloid. Once that is in place, a large portion of the contribution becomes “transport known hyperbolic constructions into a different coordinate system.” The paper is honest to some extent about using the isometry to obtain operators in **Theorem 4.3**, but the framing in the introduction and conclusion leans toward presenting PVNNs as a substantially new hyperbolic neural framework rather than, more precisely, a reparameterization of existing hyperbolic geometry with practical numerical advantages. That distinction matters scientifically, because isometric models should not change representational power, and so the burden is on the paper to show that the coordinate choice yields meaningful implementation or optimization benefits beyond cosmetic reformulation.

2. **The empirical gains on standard learning tasks are positive but not consistently strong enough to fully justify the breadth of the claimed practical advantage.**  
   The paper’s strongest evidence is in numerical stability, not downstream accuracy. In **Table 4**, the gains on CIFAR-10/100 over prior hyperbolic MLR heads are small, often within the reported standard deviations. For example, the jump from Lorentz MLR to PV MLR on CIFAR-100 is modest, and the two PV variants are nearly identical. In **Table 5**, PVNN is best on Disease, Airport, and PubMed, but underperforms LNN and even some tangent-style variants on Cora. This mixed pattern suggests that PV is not uniformly better; it seems more accurate to say it is competitive and sometimes advantageous, especially on more hyperbolic datasets. The current wording occasionally drifts closer to a general superiority claim than the evidence supports.

3. **Some comparisons are not sufficiently disentangled from architectural or implementation choices, which weakens the causal claim that PV geometry itself is responsible for the observed gains.**  
   This is especially visible in the graph section. The models in **Table 5** differ by geometry, but also inherit somewhat different layer designs from different prior works. The appendix **Table 17** makes this even clearer, although the main text already hints at this by noting different FC/activation constructions across baselines. That means the comparison is not “same architecture, only coordinate model changed” in the strict sense. Similarly, in the genome experiment, **Table 10** compares PVCNN against HCNN-S and Euclidean CNN, but the baselines are reported from a prior paper rather than rerun in the same code path according to the main text. That is convenient, but it is not the cleanest evidence for a representation-level advantage.

4. **The paper repeatedly makes efficiency claims without adequately validating them experimentally.**  
   The discussion after **Theorem 5.2** is a good example. The authors argue that the simplified score in **Eq. (19)** avoids the intermediate tensor from **Eq. (18)** and can be implemented as matrix multiplication. That sounds plausible and probably true, but there is no accompanying wall-clock or memory benchmark. Likewise, **Section 5.3** argues that direct PV activation is more efficient than tangent-space activation because it avoids \(\mathrm{Exp}_0\) and \(\mathrm{Log}_0\), but there is no timing evidence. The normalization section partly addresses cost in **Table 7**, which is appreciated, yet the broader efficiency story for PVNN as a whole remains asserted rather than demonstrated.

5. **The mathematical exposition is mostly solid, but there are places where notation and claims are looser than they should be for a theory-heavy paper.**  
   A few examples:
   - In **Theorem 4.3**, the logarithm map in **Eq. (11)** is given as \(\mathrm{Log}_x(y)=\sigma(x,y)z+\tau(x,y)\langle x,z\rangle x\), but the subsequent derivation relies on several nontrivial simplifications hidden behind the isometry argument. This is acceptable if the proof is delegated to the appendix, but in the main paper the result appears somewhat abrupt and difficult to sanity-check.
   - In **Section 5.2**, the FC definition through the system of equations in **Eq. (21)** is not especially transparent. The notation \(\operatorname{sign}(\langle d_{\mathbf{0}_k}\pi(e_k), -\mathbf{0}\oplus_{\mathrm{U}}x\rangle)d(y,H_{e_k,\mathbf{0}})=v_k(x)\) is odd, because the left side mixes a sign term based on the input \(x\) with a distance term based on the output \(y\). The theorem then produces the closed form in **Eq. (22)**, but the construction feels reverse-engineered rather than naturally motivated.
   - There are also small notation inconsistencies, for instance the model notation fluctuates between \(\mathbb{P}\mathbb{V}_K^n\), \(\mathbb{PV}_K^n\), and related shorthand, and the typography in some displayed equations is a bit messy. None of this is fatal, but it slows down careful reading.

6. **The normalization claim is stronger than what is established in the main paper.**  
   In **Section 5.4**, the authors write that PV GyroBN “can normalize sample statistics,” and after **Theorem 5.4** state that after centering the batch mean is shifted to \(\mathbf{0}\), after biasing it is translated to \(\beta\), and after scaling the variance becomes \(s^2\). But **Theorem 5.4** only states homogeneity of the Fréchet mean under gyrotranslation in **Eq. (26)** and homogeneity of dispersion from \(\mathbf{0}\) under scalar gyromultiplication in **Eq. (27)**. This is not quite the same as a complete statement about Fréchet variance after the full three-step BN transform in **Eq. (25)**, especially once the mean is moved away from \(\mathbf{0}\). I suspect the intended result is correct or nearly correct under the gyrogroup formalism, but the main-paper statement is a bit too quick relative to what is actually shown there.

7. **The stability experiments are narrowly scoped and somewhat handpicked.**  
   The numerical section uses \(K=-1\), dimension \(n=16\), and scalar multiplication as the main probe. This is a reasonable start, but it is also a friendly setting for demonstrating a coordinate advantage. The paper would be more convincing if it varied curvature, dimension, and more operator chains that occur in actual training loops. **Table 3** reports only a gradient range, which is suggestive but quite compressed; it does not show distributions, dependence on initialization scale, or sensitivity to training depth. As written, the results support that PV coordinates are stable for these selected probes, but they do not yet establish a broad claim of training robustness.

8. **The graph ablations reveal instability and inconsistency that the paper does not discuss enough.**  
   **Table 6** is mixed: PVNN is much better than PVNN+TFC on Airport, but slightly worse on PubMed and clearly worse on Cora. **Table 7** is even more concerning. The Fréchet-mean approximations do not improve monotonically with more iterations, and some settings collapse badly, especially on Airport and Cora. The “Fréchet \(\infty\)” row is not actually the best row, which is awkward given the implied interpretation. This does not invalidate the method, but it suggests that the normalization story is more brittle than the text around **Section 6.3** lets on.

9. **The paper lacks stronger evidence that direct PV-space operations are preferable to simply using equivalent Poincaré or Lorentz implementations with numerically careful parameterizations.**  
   Since the models are isometric, the practical question is not whether PV is mathematically valid, it clearly is, but whether PV is the best engineering choice. The paper compares against standard Poincaré and hyperboloid baselines, but does not investigate whether those baselines can close the gap with clipping, reparameterization, mixed precision handling, or other stability tricks. This matters because the paper’s main practical claim is about numerical robustness, not expressive power.

10. **There is no visualization or qualitative analysis helping the reader see what PV coordinates are actually doing differently.**  
   This is not mandatory, but for a paper advocating a new hyperbolic coordinate system, some geometric intuition would help. A simple plot comparing trajectories or norm distributions under PV versus Poincaré, especially near problematic boundary regions, could have made the stability claim much more tangible. The absence is noticeable because the entire paper is about representation choice, yet the empirical section is nearly all scalar benchmark tables.

## Questions
1. The strongest conceptual concern is the role of isometry. Since **Theorem 4.2** establishes PV as isometric to the Poincaré ball, could the authors sharpen the claim from “new alternative geometry” to “new coordinate model with numerical advantages,” and explain more explicitly what benefits remain after factoring out expressivity equivalence? A concise discussion of what is and is not gained by changing coordinates would increase my confidence in the contribution.

2. Can the authors provide direct runtime and memory measurements for the claims around **Eq. (19)** and direct PV activations in **Section 5.3**? I would like to see evidence that the claimed computational advantages hold in practice, not just algebraically.

3. The normalization argument in **Section 5.4** needs tightening. Can the authors state precisely what statistic is guaranteed to become \(s^2\) after **Eq. (25)**, and whether this refers to Fréchet variance, dispersion from the identity, or an approximation thereof? A short derivation in the rebuttal would help.

4. For the graph results in **Table 5**, to what extent are the gains due to geometry rather than differing layer parameterizations inherited from prior baselines? If the authors can report a cleaner “same architecture, different coordinate model” comparison, that would materially strengthen the empirical case.

5. **Table 7** is not monotone in the number of Fréchet iterations, and some rows are surprisingly poor. Can the authors explain this behavior? In particular, why is “Fréchet \(\infty\)” not consistently strongest if it is meant to represent the most accurate batch statistic?

6. For **Table 10**, were the Euclidean CNN and HCNN-S baselines rerun under the same implementation and training environment as PVCNN, or are they copied from the prior paper as stated in the text? If the latter, could the authors comment on how much variance in preprocessing or optimization might affect the comparison?

7. The numerical stability section would be stronger with broader stress tests. Do the authors have results varying \(K\), ambient dimension, precision, or composition depth of Riemannian operators? Even a compact additional table would help establish that the effect is robust.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
The paper uses standard benchmark datasets and develops general-purpose geometric learning methodology. I did not identify a concrete ethics issue from the main paper.

## Soundness Rating
3: good. The core technical story is coherent and the main claims are mostly supported, but several practical claims are only partially validated, and some mathematical statements in the main text are stronger or looser than the evidence presented there.

## Presentation Rating
3: good. The paper is generally readable and organized, though some equations and constructions in Sections 4 and 5 are dense, and a few claims around normalization and practical benefit need sharper wording.

## Contribution Rating
3: good. The paper makes a useful contribution by systematizing PV-space operators and showing that this coordinate model can be practical for hyperbolic neural networks, but the originality is somewhat limited by the explicit isometric equivalence to existing models and the empirical gains are not uniformly decisive.

## Overall Rating
6: Marginally above the acceptance threshold. But would not mind if paper is rejected. The work is technically solid and useful, especially as a stable coordinate treatment of hyperbolic neural networks, but the novelty is more model-centric than algorithmically deep, and the empirical case, while positive, is not uniformly strong enough for a clearer accept.

## Reviewer Confidence
4: confident. I am familiar with hyperbolic representation learning and geometric deep learning, and I checked the main technical flow and experimental evidence with reasonable care, though I did not independently verify every appendix proof in full detail.