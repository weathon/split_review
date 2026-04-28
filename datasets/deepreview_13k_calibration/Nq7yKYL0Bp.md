# ProtPainter: Draw or Drag Protein via Topology-guided Diffusion

- Decision: Accept
- Avg Score: 6.33
- Scores: 8, 5, 6

## Abstract
Recent advances in protein backbone generation have achieved promising results under structural, functional, or physical constraints. However, existing methods lack the flexibility for precise topology control, limiting navigation of the backbone space. We present $\textbf{ProtPainter}$, a diffusion-based approach for generating protein backbones conditioned on 3D curves. ProtPainter follows a two-stage process: curve-based sketching and sketch-guided backbone generation. For the first stage, we propose $\textbf{CurveEncoder}$, which predicts secondary structure annotations from a curve to parametrize sketch generation. For the second stage, the sketch guides the generative process in Denoising Diffusion Probabilistic Modeling (DDPM) to generate backbones. During the process, we further introduce a fusion scheduling scheme, Helix-Gating, to control the scaling factors. To evaluate, we propose the first benchmark for topology-conditioned protein generation, introducing Protein Restoration Task and a new metric, self-consistency Topology Fitness (scTF). Experiments demonstrate ProtPainter's ability to generate topology-fit (scTF $>$ 0.8) and designable (scTM $>$ 0.5) backbones, with drawing and dragging tasks showcasing its flexibility and versatility.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This work proposes ProtPainter, a diffusion-based method for generating protein backbones with topological constraints. The proposed CurveEncoder enables sketching, bridging the gap between a conditional curve and backbone modality. The sketch guided sampling based on Helix-Gating scheduling enables efficient feature fusion and retains the most generation ability of RFDiffusion. The method enables powerful topology space navigation through curve-based operations, enriching current protein design methods.

### Strengths
1.	The author provides a novel and meaningful task as Curve and topology-based protein design, which offers relatively precise and flexible global topology control. The point is the authors connect curves and SSE, which serves as a blueprint and a bridge between human-draw, maybe not so physically reasonable curves and designable protein backbones
2.	The paper proposes a simple and elegant method for curve-guided protein backbone sampling, including curve sketching and Sketch-guided backbone sampling
3.	This paper presents a simple, training-free sketch-guided backbone sampling method based on interpolation between zt and scaled y (yt-1), without the need for expensive retraining of large protein structure generative models.
4.	The author proposes Helix-Gating to improve the training-free guided sampling performance further.

### Weaknesses
1.	The proposed method underperforms when being conditioned on complex interlocking topologies, and this framework has not supported SSE annotation with beta sheets or others so far. The lack of support for beta sheets is a significant limitation, as these secondary structures are crucial for many protein folds and functions. The method's difficulty with interlocking topologies suggests a potential weakness in handling non-local interactions and complex spatial arrangements, which are common in real-world proteins. This limits the applicability of the method to a subset of protein structures.
2.	For binder design, ProtPainter just provides an empirical conformation estimation. Further optimization and validation are required. The method does not offer a robust way to optimize the generated structures for binding affinity or specificity. The lack of a clear optimization strategy and validation protocol makes it difficult to assess the practical utility of the method for binder design. The empirical nature of the conformation estimation also raises concerns about the reliability of the generated structures for downstream applications.
3.	For users facing real-world tasks, a more user-friendly, responsive interface that allows users to draw or drag proteins with ease is needed. The current interface is not intuitive, requiring users to have a good understanding of protein topology and drawing skills. This limits the accessibility of the method to a smaller group of expert users. The lack of user-friendly tools for curve manipulation hinders the practical application of the method for real-world protein design tasks.

### Questions
1.	The main experiments are based on Protein Restoration task. Is it difficult for a general user to draw a reasonable curve?
2.	To draw a good curve requires both drawing skills and knowledge about protein topology, if the drawn curve is not so good (for example, the drawn global topology is not physically stable), will the generation performance drop?
3.	Do the authors have some ideas about correcting the draw error mentioned in the the Q2?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper tackles controllable protein structure generation. Specifically, it proposes a method to extract an editable "curve representation" that describes the chain together with some secondary structure annotations from protein backbones. Given that curve, new proteins with a similar topology can be synthesized by conditioning a protein backbone generator on the curve. Modifying the curve representation enables to edit the protein structure in a controllable manner. The curve representation is extracted from given proteins using a CurveEncoder module. The method is validated on protein restoration tasks where the goal is to reconstruct proteins with similar topology as the input proteins from which the curve representation was extracted. Additionally, some editing tasks are shown that topologically and spatially modify given proteins.

### Strengths
**Originality**: The proposed method is novel, to the best of my knowledge, building on the conditioning framework from Choi et al. (ILVR). Some related works exist, however, and the method is quite related to DiffTopo.

**Experiments**: The paper successfully demonstrates that the curve representation can encode spatial protein layout and topology and that it can be used to recreate proteins of similar topologies. The qualitative protein editing experiments are also interesting.

**Clarity**: While it is overall possible to generally follow the paper, the paper writing is of poor quality and some things remain somewhat unclear (see weaknesses below).

**Quality and Significance**: Due to the paper's weaknesses (see below), I think the significance and quality of the paper is low.

### Weaknesses
I see several weaknesses:

- The method can only generate alpha helices or coil/loop regions, but not beta sheets. This is a major weakness and severely reduces the method's broad applicability and significance. This is also not discussed in detail and it remains unclear why exactly that is the case. Why can beta sheets not be treated similarly like alpha helices?
- The only experiment where ProtPainter is compared to existing baselines is in Table 3. However, I think these results are misleading. These baseline models (RFDiffusion, Chroma, and ProteinGenerator) are not conditioned on topological, spatial layouts of the proteins, it seems, as is the case for ProtPainter. Hence, we cannot expect those models to spatially and topologically recreate any given proteins and it is not surprising that those baselines achieve low scTF/FD scores (and for designability [CD], ProtPainter isn't actually outperforming the baselines in all cases). In other words, the baselines are not chosen appropriately.
  - Chroma has a method to constrain protein generation on shapes. I think it could be appropriate to extract shapes from the input proteins (analogous to the curves) and condition Chroma on those, if possible.
  - I also think comparisons to TopoDiff and/or DiffTopo would be appropriate, if possible. They may not offer fine editing control, but these methods can also encode protein topologies and spatially reconstruct, I think. These works are actually discussed in the paper and are arguably most related.
- The designability definition used in this paper relies on pLDDT > 70 and scTM > 0.5. However, most works in the literature these days use a stricter designability definition of scRMSD < 2 Angstrom. I would suggest the authors to use this instead.
- In Section 3.2, the paper writes that ProtPainter leverages RoseTTAFold to predict $\hat{z}_0$ (also in figure 1). I would have thought that the authors use the diffusion model RFDiffusion (which is initialized from RoseTTAFold, but itself is not a folding model anymore after training). This also isn't well explained in the very short "Train" section in the appendix. It is not entirely clear how the model is trained.
- The model only shows protein restoration and protein editing tasks, but no de novo generation from scratch. It would be great if the authors could also demonstrate the generation of designable proteins from curves drawn entirely from scratch or generated by another curve generator (the very related TopoDiff and DiffTopo do such things, too).
- As mentioned previously, the writing quality is generally low, with various grammar errors. This negatively affects the quality of the paper.
- The ILVR method is cited, but without looking at the Choi paper the ProtPainter method is hard to follow in detail. More details would be helpful and a more critical discussion and motivation of the chosen frame filter operation would be useful, among other things, for example.

### Questions
I do not have any further questions to the authors.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a conditional diffusion model that can generate proteins corresponding to 3D topological designs provided by the user.

### Strengths
This paper defines a new task, which is a novel attempt, even though I think the significance and novelty of this task may be questionable. The paper introduces CurveEncoder and Helix-Gating for this task, presenting certain innovativeness in its methodology.

### Weaknesses
1. The definition of this task may be highly similar to the definition of a problem in chroma [1], although not exactly the same. Here, I first point out where chroma mentions the corresponding task. Figure 3 in the main text of chroma indicates that they have implemented shape conditioning to enable geometric molecular programming. Section R of chroma's supplementary materials, titled "Programmability: Shape," also discusses this. My perspective is that while the objectives of this part of chroma and ProtPainter are not perfectly aligned, the desired effects are very similar. Furthermore, it might be possible to simply adjust chroma's Conditioners to transform chroma's Shape Conditioners into topological Conditioners. My question is: How does ProtPainter's topological conditioning differ from or improve upon Chroma's shape conditioning? Are there specific advantages or capabilities that ProtPainter offers that cannot be achieved by adapting Chroma's approach?


2. A major difference between ProtPainter and chroma's Shape Conditioner is that ProtPainter can additionally specify the proportion of secondary structures, such as the percentage of Helices. However, I think that in many cases when designing the protein scaffold, we want more helical-like secondary structures, as they can improve the thermal stability of the protein. Therefore, specifying the proportion of Helices is unnecessary. Because we don't need low proportion of Helices. It is only when designing motifs or some flexible regions, or under special circumstances, that one would want to avoid Helices and thus need to specify their proportion. But these special circumstances are usually quite complex, and merely specifying topology may be insufficient and unnecessary. Thus, I do not fully understand the significance of this aspect. Of course, I understand that protein design is a very complex issue, and the scenario I mentioned above might only represent one type of design problem. There may be other types of design problems where the user needs to specify the percentage of helices; however, I do not understand the importance of this issue. The paper does not seem to particularly discuss this matter either. Please have the author indicate whether specifying the percentage of helices is important. If it is important, could you explain why and provide applications along with relevant papers?


3. Whether users can provide a correct 3D topological blueprint for successfully generating a protein is questionable. The sketches provided to the diffusion model in this paper are all derived from real proteins. However, in real application scenarios, it is doubtful whether researchers can provide such accurate sketches. If researchers cannot provide very valid sketches, it is uncertain whether ProtPainter can function properly. Moreover, if researchers cannot provide very valid sketches, then chroma's Shape Conditioner might be a more reasonable approach. I suggest that the author provide dedicated experiments to analyze this issue. For example, 1) conduct a user study where a person sketches a protein based on their understanding and professional knowledge of proteins, and then check how successfully ProtPainter can design the protein according to this sketch. 2) In the paper, sketches of proteins are generated from real proteins. During inference, adding noise to the actual sketches to simulate user errors and randomness, see if ProtPainter can still smoothly generate proteins. Additionally, analyze the maximum level of noise that ProtPainter can tolerate.

### Questions
See Weaknesses

### Soundness
2

### Presentation
2

### Contribution
2
