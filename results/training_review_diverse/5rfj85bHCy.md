Now I have all the information I need. Let me synthesize the final review.

## Analysis of Harsh Critic Claims vs. Paper

**Claim 1 (β undefined):** Paper mentions β in lines 164 and 168, says it's "similar to" prior work, and states β=1 initialization. The forward pass Eq. (3) defines H^(l) but doesn't include β. The critic is correct that the residual connection equation involving β is never formally given. **Keep as minor** — inferable from prior work citations but should be explicit.

**Claim 2 (α regularization undermines adaptivity):** Paper states the regularization "encourages smoother solutions and prevents the network from introducing excessive non-linearity" (lines 177-178). No ablation is provided. This is a defensible design choice, but an ablation would strengthen the paper. **Keep as minor.**

**Claim 3 (RBF hyperparameters unspecified):** Paper mentions Wendland C⁴ kernels with trainable centers and scales τᵢ (lines 200-213), but does not state number of centers, initialization strategy, or computational cost. **Keep as minor/major** — these are needed for reproducibility.

**Claim 4 (results not available):** Results are in `\input{...}` files that the parser did not expand. Per instructions, this is a parser artifact. **Remove.**

**Claim 5 (no truly discontinuous benchmark):** Allen-Cahn has steep fronts but is technically smooth. Darcy Flow is smooth. The paper claims to handle "discontinuities" but tests only on smooth problems with sharp transitions. **Keep as minor** — reasonable critique about scope/evaluation coverage.

**Claim 6 (robustness claim unsubstantiated):** Abstract says "more robust to training point locations and neural network architectures" but no experiment varies these. **Keep as major** — this is a concrete claim without evidence.

**Claim 7 (background vs. contribution balance):** Subjective judgment, partly merges with point 3. **Remove / merge into point 3.**

Now let me handle the Strength Finder's output. Strength 4 ("Thorough and fair empirical evaluation") is partially true but conflicts with the verified weakness about the unsubstantiated robustness claim and missing RBF details. I'll keep the strength that the paper compares against 5 baselines, but qualify it.

Let me write the final review.

---

Actually, I want to be careful. The robustness claim - is it possible this evidence is in the `\input` files? The `\input{results_overview}`, `\input{06-AC_experiments}`, `\input{06-DF-smooth_experiments}`, `\input{06-DF-rough_experiments}` files? Possibly. But from the text I have, the robust claim appears only in the abstract. The critic is working from the same text I have. Without seeing those input files, I can't confirm whether robustness experiments exist. However, the rules say the parser strips sections - these are present in the original. 

Hmm, but the critic's point is specifically about the claim in the abstract not being substantiated. Even if the results files contain more experiments, there's no mention in the visible text of architecture or training point variation experiments. Let me look at the experiment section headers again:

Line 261: `\input{06-AC_experiments}` - Allen-Cahn experiments
Line 281: `\input{06-DF-smooth_experiments}` - Darcy Flow smooth
Line 282: `\input{06-DF-rough_experiments}` - Darcy Flow rough

These are experiment subsections. They could potentially contain robustness experiments. But the section title (Darcy Flow) and the problem statement suggest these are about specific PDE benchmarks, not general robustness studies.

I think it's safe to say the robustness claim is not substantiated in the text I can see. But should I remove it because the evidence might be in the input files? The instruction says "REMOVE weaknesses about missing appendix, missing proofs in appendix, or absent references." But this isn't about appendix — it's about a substantive claim in the abstract that should be supported by experiments described in the main text. Let me keep it as a verified weakness since there's no mention of such experiments anywhere in what's available.

OK, finalizing my review now.## Summary

HyResPINNs introduce a novel PINN architecture that combines standard DNN and RBF network outputs in each residual block via a learnable convex combination parameter α, alongside adaptive skip connections (β) between blocks. The core idea is that the DNN captures smooth global behavior while the RBF network captures sharp local features, with the balance learned during training. The paper evaluates on Allen-Cahn (1D/2D) and Darcy Flow (2D/3D) problems against five baselines.

## Strengths

1. **Novel adaptive hybrid residual blocks with principled mixing.** Each block computes a sigmoid-gated convex combination of a DNN output and an RBF output via a trainable α parameter (Eq. 4). This is a genuine architectural innovation over prior residual blocks (PirateNets, StackedPINNs) that mix only input and residual — here the model can dynamically allocate representational resources between a smooth global approximator and a local one. The paper reports that learned α values differ meaningfully across problems, confirming the adaptivity is utilized.

2. **Consistent accuracy gains across multiple benchmarks.** The paper compares against five baselines (PINN, ExpertPINNs, ResPINNs, PirateNets, StackedPINNs) on the same hyperparameters across 1D Allen-Cahn, 2D/3D Darcy Flow with Dirichlet and Neumann BCs. Table 1 (referenced in the text) consistently reports lower relative L² errors, with the abstract claiming "orders of magnitude" improvement on certain problems. The qualitative comparison (Figure 3) visually shows HyResPINNs capturing sharp interfaces where standard PINNs fail.

3. **Practical RBF design via compactly supported Wendland kernels.** The choice of Wendland C⁴ kernels (compact support, sparse kernel matrices) is well-motivated: it keeps added computational cost modest while providing local approximation power. The scale parameters τᵢ are trainable, and Figure 2 shows learned kernels adapting their width to local solution features.

4. **Fair experimental setup.** All methods are trained under identical hyperparameters, following established experimental procedures from prior work (Wang et al. 2022, 2023, 2024). The use of standard training infrastructure (A100 GPU, libtorch) is clearly stated.

## Weaknesses

### Fatal
None.

### Major

1. **The claim of robustness to training point locations and architectures is asserted but not demonstrated.** The abstract states "HyResPINNs are more robust to training point locations and neural network architectures than traditional PINNs" — but no experiment in the visible text varies training point distributions, network widths, depths, or architectural choices. This is a concrete, falsifiable claim that the paper does not support with evidence. It either needs to be substantiated or removed from the claims.

2. **Critical RBF hyperparameters are underspecified, hampering reproducibility.** The paper never states: (a) how many RBF centers are used per residual block, (b) how centers are initialized (random subset of collocation points? grid?), (c) how the number of centers is chosen across different problem sizes, or (d) the wall-time / computational cost relative to baselines. The paper claims "modest increases in training costs" but provides no runtime comparison. Since the RBF network is half of the paper's core architectural novelty, these are not secondary details — they determine whether the method is practically viable and how its performance depends on user choices.

### Minor

3. **The β adaptive skip-connection parameter is mentioned but never formally defined in an equation.** Lines 164 and 168 state β is "similar to" prior work (PirateNets, StackedPINNs) and initialized to 1, but the forward pass equation (Eq. 3) gives only H^(l). The actual residual update — whether `x^{(l+1)} = β^{(l)} x^{(l)} + (1-β^{(l)}) H^{(l)}` or `x^{(l+1)} = x^{(l)} + β^{(l)} H^{(l)}` — is never specified. Since adaptive skip connections are advertised as a key feature, this should be explicit rather than deferred by reference.

4. **The α² regularization is neither justified nor ablated.** The total loss includes λₚ Σ αᵢ² to "encourage smoother solutions" and "prevent the network from introducing excessive non-linearity" (lines 177–178). This penalizes large α, biasing toward the smooth DNN. If sharp features are present, the optimal α may be large, and this regularization could harm accuracy. No ablation or sensitivity analysis is provided, and no guidance is given on how λₚ is selected. The claimed adaptivity would be stronger if shown to work without (or with minimal) such bias.

5. **The paper emphasizes handling "discontinuities" but tests only on smooth problems with steep gradients.** The introduction and motivation repeatedly mention "discontinuous solutions or sharp interfaces" and "discontinuous or sharp features." However, Allen-Cahn (steep front, technically smooth) and Darcy Flow (elliptic, smooth) are both smooth problems. No benchmark with true shocks, discontinuities, or singularities (e.g., Burgers' equation with shock, advection-dominated problems) is included. This weakens the link between the method's design rationale and its evaluation.

### Trivial
None.

## Nice-to-Haves
- An ablation study comparing HyResPINNs with and without the α² regularization on a problem where sharp features dominate, to demonstrate whether the penalty helps or hinders.
- A truly non-smooth benchmark (e.g., Burgers' with shock) would strengthen the connection between the method's motivation and its demonstrated capabilities.
- A wall-time comparison against all baselines to substantiate the "modest increases in training costs" claim.

## Removed Points
- **Critic's Point 4 (results not accessible):** The experimental results are embedded via `\input{...}` commands that the parser could not expand. This is a parser limitation, not an author error — the results exist in the original submission. Removed per the rule that parser-stripped content should not count as a paper flaw.
- **Critic's Point 7 (background vs. contribution balance):** Subjective presentation judgment. The relevant substantive sub-concerns (missing implementation details) are already captured in Weakness 2 above.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Formalize the forward pass with β: add an equation `x^{(l+1)} = g(β^{(l)}, x^{(l)}, H^{(l)}(x^{(l)}))` and state whether β is scalar or elementwise and how it is constrained.
2. Substantiate or remove the robustness claim from the abstract — either add experiments varying training point distributions and network architectures, or drop the claim.
3. Report RBF center count, initialization scheme, and wall-time comparison for every experiment.
4. Add an ablation removing the α² penalty on at least one problem to demonstrate whether the regularization is necessary or whether the adaptivity works on its own.

## Score and Decision

**Originality:** Good — hybrid NN+RBF residual blocks with learned mixing is a novel architectural contribution.

**Importance of research question:** Relevant — improving PINN accuracy on problems with sharp features is an active area.

**Claims supported:** Partially — the core accuracy claim is supported; the robustness claim is asserted without evidence; the architectural specification has gaps.

**Soundness of experiments:** Adequate in setup (multiple baselines, identical hyperparameters), but missing RBF operational details and robustness experiments weaken it.

**Clarity of writing:** Reasonably clear in the method description, but the β equation omission and missing RBF details are gaps.

**Value to community:** Moderate — the core idea is useful and could inspire further work, but the paper needs to close the specification gaps to be reproducible.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>