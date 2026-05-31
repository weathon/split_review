## Human Reviewer 1

### Summary
Using a stable sparse autoencoder, the paper builds a large concept dictionary for DINOv2 and shows task-specific feature usage. Analyses of concept statistics and geometry reveal distributed, partially sparse structure that only partially matches the Linear Representation Hypothesis. Finally, the authors propose the Minkowski Representation Hypothesis: token embeddings lie in sums of convex regions (aligned with multi-head attention’s convex mixing), which have implications in mechanistic interpretability such as model steering.

### Strengths
Clarity:
- The paper follows a mostly logical narrative structure: Testing LRH with Stable SAE -> Empirical findings on concept statistics and geometry -> MRH
- Once released, the interactive concept explorer can make the work much easier to visualize.

Quality:
- The methodology is rigorous, relying on quantitative measures for its major claims (singular-value spectra, coherence vs Grassmannian/random baselines, etc).
- The convex-hull constraint on the SAE makes it more reproducible by keeping concepts in-distribution. 

Originality:
- While concepts such as superposition and polysemanticity have been widely explored in mechanistic interpretability, the idea of convex regions is quite novel in this area, to the best of my knowledge.

### Weaknesses
l161: Because the stable SAE constrains dictionary atoms to the convex hull of activations, convexity is guaranteed for the learned concepts but not necessarily for the native representation. Maybe explicitly separate SAE-induced claims from “model-native” claims, and add ablations with unconstrained SAE, showing the same qualitative geometry without the convex prior.

l064: The importance definition is clear, but the figure mapping isn’t. Maybe specify exactly what dot size and color encode in Figure 1. Adding a concise legend in the main text, a one-line formula linking $\phi$ to the plotted quantity would make the visualization reproducible and easier to see.

l259: UMAP is fine for intuition, but it shouldn’t be used to make claims. Maybe caution that UMAP as visualization only, add a brief hyper-parameter sensitivity (n_neighbors, min_dist, seed) in the appendix, and keep the main analysis on PCA/spectral metrics.

l293: "dense Sun et al. (2025) activations" -> "dense activations Sun et al. (2025)"

### Questions
See weaknesses.

### Soundness
2

### Presentation
3

### Contribution
4

### Rating
8

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper introduces a 32k-concept dictionary extracted from DINOv2 using Sparse Autoencoders (SAEs) and presents an interactive web-based visualization platform. The authors analyze how downstream tasks selectively recruit concepts from this dictionary, finding that classification relies on "Elsewhere" concepts implementing object negation, segmentation uses boundary detectors forming coherent subspaces, and depth estimation draws on three families of monocular cues (projective geometry, shadows, and frequency transitions). The work proposes the Minkowski Representation Hypothesis (MRH) as an alternative to the Linear Representation Hypothesis (LRH), suggesting that token embeddings behave as sums of convex regions around archetypal landmarks rather than as sparse combinations of near-orthogonal directions. However, the authors acknowledge that MRH remains a working hypothesis requiring further empirical validation.

### Strengths
**Clear introduction and methodological foundation**: The paper provides adequate background on ViTs, DINOv2, vision explainability, SAE adoption, and task-specific learned concepts, making the work accessible to the broader audience.

**Interpretability contributions**: The interpretation sections are particularly well-executed, and the release of a web-based visualization platform for navigating DINOv2's 32k-concept dictionary represents a valuable resource for the community.

**Technical rigor**: The submission is mostly clear, technically correct, and results appear reproducible given the extended mathematical explanations, despite code not being provided.

**Novel theoretical perspective**: The paper proposes MRH as an interpretability framework for understanding ViTs, suggesting future research should examine these models through this geometric lens.

### Weaknesses
**Limited scope of downstream task exploration**: Section 3 examines only three downstream tasks, while DINOv2 supports many more applications. For classification, only the "elsewhere" concept is explored in detail, limiting the generalizability of findings.

**Insufficient empirical foundation for MRH**: The authors propose MRH based on intuitions from task-specific geometrical organization but acknowledge it still needs rigorous proof (line 445). Given the limited number of tasks and task-specific concepts explored (see point above), the theoretical proposition rests on unstable empirical grounds.

**Underdeveloped discussion of implications**: The paper lacks sufficient explanation of what consequences adopting the MRH concept has for interpreting ViTs and what concrete benefits this perspective provides to the research community. The discussion section should match the verbosity and clarity of the introduction.

**Minor:**
- Misleading characterization of SAE contribution: The authors state they "operationalize" LRH using SAE, when they actually adopt an SAE previously introduced by Fel et al. (2025). This overstates their methodological contribution.
- Excessive reliance on appendix: Figures in the appendix are cited frequently in the main text (e.g., "Different tasks recruit different concepts" in Sec. 3, "Empirical evidences" in Sec. 6), resulting in sections that are difficult to follow without constant back-and-forth navigation.
- Citations should stay in brackets, use \citet.
- TL;DR is broken.

### Questions
- Sec. 3: what's the reason for isolating the top 100 most task-aligned concepts per-head when analyzing their similarities?
- Sec. 3: how do you defined the top concepts for classification and how important or frequent is the "elsewhere" concept? why only this concept is analyzed for the classification task?
- Sec. 3: you cite Fig.10 (right) in appendix but the same can be seen in Fig. 2
- Is "the largest interactive interpretability demo" (line 112) an advantage? isn't complexity a problem for interpretability?
- What's the x-axis of Fig.11 left?

### Soundness
3

### Presentation
4

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 3

### Summary
In this work, the authors analyze the internal representations of the DinoV2 model to provide interpretability insights into how the model performs tasks. They begin by characterizing tokens using a sparse autoencoder to create a concept dictionary. They then investigate how different tasks use this dictionary to accomplish their distinct goals and highlight their distinct differences. For example, they find that classification uses elsewhere concepts while segmentation uses boundary detectors. Secondly, the authors find that the representations are partially dense demonstrating behavior that may be inconsistent with sparse coding. Finally, the authors propose a new hypothesis called the Minkowski Representation Hypothesis which they suggest as an alternative to the LRH. They provide initial evidence for the hypothesis, then leave room for investigations in the future.

### Strengths
This paper demonstrates clear novelty and depth while providing a useful tool for other researchers to investigate further. These qualities constitute a clear accept.

### Weaknesses
The analysis in this paper is mostly descriptive as opposed to describing why different tasks within DINOv2 have different representational sparseness etc.

### Questions
One weakness of this paper is that it primarily is descriptive as opposed to providing an understanding of why each task has such different utilization of concepts. Can the authors describe why they believe this asymmetry is happening? Is it relative complexity between the task types etc?

The authors suggest that Dinov2’s representations follow their proposed Minkowski Representation Hypothesis. One thing that isn’t clear is whether the authors believe that other networks should follow this hypothesis. It seems to stem very naturally from attention layers. Do the authors expect other networks to follow this hypothesis? If so, when do they expect it to emerge over LRH or do they consider it an alternative hypothesis to LRH in general?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
8

### Confidence
2

---

## Human Reviewer 4

### Summary
The paper studies what DINOv2 “sees” by operationalizing the Linear Representation Hypothesis (LRH) with a sparse autoencoder to extract a 32k-concept dictionary from ViT activations, then analyzing how downstream tasks recruit these concepts and what the concepts’ geometry suggests. Empirically, different tasks use distinct, low-dimensional subsets: classification leans on off-object “Elsewhere” concepts, segmentation concentrates on boundary detectors, and depth estimation draws on monocular cue families. they also run geometric diagnostics and find some deviations from the LRH like structured redundancy. Motivated by this, the authors propose the Minkowski Representation Hypothesis (MRH): token embeddings lie in Minkowski sums of convex polytopes spanned by archetypal landmarks, a structure they argue multi-head attention realizes via convex combinations per head and summation across heads. They provide preliminary qualitative/quantitative signals consistent with MRH - e.g. token embeddings smoothly interpolate between landmark-like prototypes instead of varying along linear feature axes.

### Strengths
- The paper is ambitious in scope, undertaking one of the first large-scale interpretability analyses of a state-of-the-art vision foundation model through SAEs. 
- Goes beyond static visualization to quantify how distinct downstream tasks (classification, segmentation, depth) selectively recruit different subsets of the concept space, revealing functional specialization. e.g. the paper identifies interpretable and generalizable phenomena—e.g., “Elsewhere” (off-object) concepts, border detectors, and monocular depth cues—illustrating that meaningful, task-specific structure emerges spontaneously in DINO.
- Moves beyond the traditional “sparse direction” view of representations to analyze the geometric structure (anisotropy, coherence, spectra) of learned concepts
- The work also makes a creative theoretical leap—proposing the Minkowski Representation Hypothesis to reinterpret transformer geometry in terms of convex archetypal regions, an idea that elegantly ties attention mechanics to cognitive theories of conceptual spaces.

### Weaknesses
- The paper attempts to do too much—spanning SAE implementation, large-scale task analysis, and a new geometric theory (MRH)—without a unifying throughline. The connection between these parts often feels narrative rather than logically necessary.
- The evidence for the Minkowski Representation Hypothesis is largely qualitative and circumstantial (e.g., UMAPs, smooth PCA maps, block structures). Stronger quantitative tests or falsifiable predictions are needed to substantiate the claim.
- The observed deviations from LRH (anisotropy, coherence, low-dimensional task subspaces) could be explained by simpler mechanisms such as structured sparsity or normalization effects—yet the paper moves quickly to a new geometric framework without ruling these out.
- Key hyperparameters (e.g., SAE sparsity level, dataset etc.) and their sensitivity are not well explored; it is unclear how robust the reported concept structure for the 3 tasks is to these design choices.
-  While task specialization is interesting, it remains correlational; it’s unclear whether manipulating the discovered concepts truly affects task behavior. I think some causal manipulation could be interesting too.

### Questions
- How do you quantitatively assess convex regions or Minkowski sums beyond analogy to attention mechanics?
- How sensitive are the learned concept dictionaries to SAE initialization and regularization strength?
- How do the discovered “Elsewhere” concepts improve human interpretability or model steering compared to prior SAE- or NMF-based approaches?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3