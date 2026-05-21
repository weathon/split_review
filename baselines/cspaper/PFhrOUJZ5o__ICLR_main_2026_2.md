---
job_id: 9536c42d-d2c7-4244-ae99-1d684c496704
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: PFhrOUJZ5o.pdf
paper: LAION-COMP: Unlocking Controllable and Compositional Generation with Structural Annotations
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, focusing on generative models, structured conditioning with scene graphs, datasets/benchmarks, and representation learning for vision.

## Minimum Quality
Pass ✅. The paper contains the necessary components for a scientific submission, including abstract, introduction, related work, dataset/method description, experiments, quantitative/qualitative results, and conclusion. While there are important concerns about novelty, evaluation design, and clarity, these are review-level weaknesses rather than desk-rejection-level defects.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions to automated reviewers, or other suspicious content targeting the review process in the provided paper text and figures.

# Expected Review Outcome:
## Summary
This paper introduces LAION-Comp, a large-scale dataset of 540K+ aesthetic images annotated with scene graphs containing objects, attributes, and relations, constructed from LAION-Aesthetics using a multimodal LLM plus partial human verification. The paper also trains several scene-graph-conditioned image generation baselines on diffusion and flow-matching backbones, proposes CompSGen Bench for evaluating complex compositional generation, and presents an SG-based image editing framework in the appendix.

## Strengths
The paper tackles a real and important problem. Compositional failures in text-to-image generation are still common, especially when multiple objects, attributes, and relations must be jointly satisfied, and a dataset-level intervention is a reasonable direction rather than yet another inference-time control trick. I appreciate that the paper does not only claim “scene graphs might help,” but actually builds a fairly large resource and trains multiple backbones on top of it.

The scale of the dataset is a practical strength. A 540K scene-graph-annotated image corpus is substantially larger than classical SG datasets such as Visual Genome, and the paper makes a credible case that existing SG datasets are too small and too spatially biased for modern high-capacity image generation. The statistics in **Table 1** and the distribution plots in **Figure 4** are useful here. In particular, **Table 1** suggests that LAION-Comp annotations contain more explicit object information than the original LAION captions, and **Figure 4(b)** indicates that relations/attributes are not completely dominated by a tiny handful of labels. Even though I have concerns about how some of the quality claims are measured, the dataset curation effort itself is nontrivial.

The qualitative examples are generally compelling. **Figure 5** makes the central claim visually understandable: the SG-conditioned models often recover object identities and relations that the prompt-only or earlier SG baselines miss. The first row is a good example of a relation that is easy to mangle with text alone. Also, **Figure 1** is effective as a motivating figure, because it shows the exact failure mode the paper wants to address, namely object/relation/attribute inconsistencies in crowded scenes.

The empirical section includes multiple backbones rather than a single cherry-picked architecture. Training SG-conditioned variants of SDXL, SD3.5, and FLUX makes the story broader than “our conditioning happens to fit one model.” In **Table 2**, the within-family comparison is the most convincing part: for the same model family, training on LAION-Comp tends to improve SG-IoU / Entity-IoU / Relation-IoU relative to training on COCO or Visual Genome. That supports the paper’s data-centric thesis better than cross-model comparisons do.

The proposed SG conditioning is lightweight in spirit. The paper adds a graph encoder on top of pretrained text encoders and injects its output into existing generators, which is a practical design choice. The architecture diagram in **Figure 12** also helps the reader understand the intended flow of object/triple embeddings into the generator.

Finally, the idea of using the same structural representation for both generation and editing is appealing. Even though the editing part is mostly outside the main paper, **Figure 6** presents a coherent interface story: SGs are not just training labels, they can act as an explicit control layer for object-level editing.

## Weaknesses
1. **The novelty claim is overstated, and the paper is not positioned sharply enough against closely related prior work.**  
The submission repeatedly frames itself as filling a major resource gap by constructing a large-scale LAION-based structural dataset and training SG-conditioned SDXL-style baselines on top of it. However, the paper’s positioning against prior large-scale structurally annotated LAION-style efforts is weak. On **Page 4**, the paper says it is extending LAION-Aesthetics with structured annotations and contrasts itself vaguely with “contemporaneous effort (Chen et al., 2024b),” but this is not enough. The paper needs a much sharper articulation of what is actually new here relative to prior LAION-derived structural annotation efforts, what exact annotation ontology differs, what scale/quality advantage is unique, and what model/training pipeline meaningfully goes beyond prior SG-conditioned diffusion work. As written, the contribution can read as “bigger LAION + GPT annotation + standard SG encoder + benchmark,” which is useful, but more incremental than the introduction suggests. This matters because ICLR main-track standards are not just about engineering effort, they are about a clearly differentiated scientific contribution.

2. **The central evaluation pipeline is too circular and fragile, because key metrics depend on GPT-4/GPT-4o extracting scene graphs from generated images.**  
This is the biggest technical concern in the paper. On **Page 6** and in **Appendix A.7**, SG-IoU, Entity-IoU, Relation-IoU, and especially the proposed annotation-quality variants SG-IoU+, Entity-IoU+, Relation-IoU+ are all based on LLM/VLM-extracted scene graphs from images. That means the paper is effectively measuring one imperfect vision-language parser against annotations generated by another closely related automated process. This is not a small implementation detail, it directly affects the validity of the headline conclusions in **Table 1**, **Table 2**, and **Table 3**. If the extractor systematically favors certain relation phrasings, certain object vocabularies, or scene-graph-like descriptions, then the benchmark can reward stylistic compatibility with the parser rather than genuine compositional correctness. The paper acknowledges hallucinations in **Figure 10**, **Figure 11**, and Appendix A.8, but those are treated as minor annotation issues rather than a broader evaluation validity problem. This matters because many of the gains claimed are on exactly these parser-mediated metrics.

3. **The paper uses “accuracy” in a mathematically misleading way for human verification, and Equation (3) does not measure what the text claims.**  
In **Appendix A.5**, the paper defines  
\[
\text{Accuracy} = \frac{\text{Actual Occurrences}}{\text{Occurrences in Annotations}} \tag{3}
\]
and immediately notes that “This definition is similar to recall.” That sentence is already a red flag. The numerator/denominator correspond neither to standard accuracy nor to standard recall unless the matching procedure and false positives/false negatives are precisely defined. If “Actual Occurrences” means correctly present annotated elements, then the quantity is much closer to precision of annotations, not accuracy. More importantly, there is no complementary estimate of missing objects/relations that the annotator failed to include, so the human verification only checks one side of annotation quality. A scene graph can have high “precision” while still missing large portions of the scene. Since the paper repeatedly uses these numbers, for example the 98.8/97.5/95.7 figures on **Page 5** and **Table 6**, to argue that the dataset is highly reliable, this definitional sloppiness matters.

4. **The benchmark is not sufficiently independent from the dataset construction process, which weakens the strength of the empirical claims.**  
CompSGen Bench is introduced on **Page 6** by selecting 20,838 “complex scenes” from the paper’s own LAION-Comp test split, specifically those with more than four relations. This means the benchmark inherits the annotation style, ontology, and possible biases of the same automated construction pipeline. It is therefore not a clean external test of compositional generalization. The paper does include some evaluation beyond this, but the main benchmark narrative is still tightly coupled to the dataset. Even the “generalization analysis” in **Appendix A.15** is not presented in the main paper, and the core tables in the main paper remain dominated by the in-distribution benchmark. This matters because a paper making strong claims about “unlocking controllable and compositional generation” should demonstrate robustness beyond its own annotation ecosystem.

5. **The methodological description of the scene-graph encoder is too underspecified for a main-track paper.**  
Section 4 and **Equation (1)** on **Page 7** present the conditioning as
\[
\mathbf{e}_{sg}=f(sg)=\text{concat}(\mathbf{e}_{t}+\alpha\mathbf{e}_{r},\mathbf{e}_{s}),
\]
but many critical details are missing or deferred. For example: what exact graph is passed to the GNN, how are multi-word relations aggregated, what message-passing operator is used, how many nodes/edges correspond to attributes, whether the GNN processes the whole graph jointly or triple-wise, how concatenated sequences are aligned with text token positions expected by the backbone, whether there is any masking/truncation for long SGs, and how conditioning length interacts with transformer cross-attention limits. The main paper says “More calculation details can be found in Sec. A.9.3,” but the main-paper method should still specify the actual learned object. As written, the core algorithm is too abstract for careful assessment.

6. **There are mathematical and notation issues around the training objective and backbone adaptation.**  
The flow-matching objective in **Equation (2)** is standard-looking,
\[
\mathcal{L}=\mathbb{E}_{x_{0},\epsilon,t,sg}\left[\| v_{\theta}(z_t,t,f(sg))-(\epsilon-x_0)\|_2^2\right],
\]
but the paper blurs what parameters are actually optimized. On **Page 7**, it says “We train the parameters of SG encoder to minimize the gap,” which sounds like the backbone is frozen, but elsewhere it says the model is “fine-tuned” and presents backbone-specific integration for SD3.5-SG and FLUX-SG. It is not clear whether only the SG encoder is trained, whether conditioning layers are trained, or whether portions of the base generator are updated. That ambiguity matters for both fairness and interpretation of performance gains. Similarly, in the SDXL case in **Appendix A.9.3**, **Equation (6)** writes
\[
\mathbf{e}_{r} = \operatorname{GNN}(E_T(triple^{sg})),
\]
which is a strange shorthand because a GNN normally consumes a graph-structured set of node/edge features, not a single triple embedding. The surrounding text says objects are nodes and relations are edges, but the equation compresses this into something that does not clearly represent the actual computation. This is not a cosmetic complaint, it makes the method harder to verify.

7. **The comparison protocol is not fully fair across input modalities, and some claims are therefore overstated.**  
The paper compares prompt-only T2I models against SG-conditioned models in **Table 2** and **Table 3**, but the input modalities are fundamentally different. Appendix **A.12.1** states that for the T2I model on LAION-Comp, the scene graph is “semantically concatenated into text” for generation, while SG2IM models use graph embeddings directly. That is not a neutral baseline for “text vs structure,” because it changes both representation and possibly prompt engineering quality. In addition, some competing methods such as SGDiff originally use bounding boxes, and although the authors retrain SGDiff without boxes for fairness, the resulting system is not necessarily the strongest version of that baseline. The paper should be much more careful in claiming superiority over “advanced scene-graph-based methods” when some baselines are adapted into a less favorable regime.

8. **The empirical gains, while real, are not consistently strong enough to support some of the paper’s broader rhetoric.**  
The strongest case comes from semantic metrics, but the image quality side is less clear. In **Table 2**, FLUX.1-Dev has FID 26.2 while FLUX-SG has 24.7, which is modest. SD3.5-Medium has FID 24.6 while SD3.5-SG has 20.8, better but still not dramatic relative to the strength of the claims. In **Table 3**, the gains on CompSGen Bench are more convincing on SG-IoU than on FID/CLIP. This suggests the real takeaway is narrower: structured annotations improve measured compositional faithfulness, not that the paper broadly solves controllable compositional generation. The conclusion on **Page 9** and the title both overreach relative to the evidence.

9. **Several important results live in the appendix, while the main-paper narrative leans on them heavily.**  
The introduction claims reliable human verification, strong editing performance, and auxiliary benchmark validation, but many of these are only substantively described in the appendix. For instance, the editing framework is introduced in the main paper and then immediately deferred to **Sec. A.1**; the human verification percentages cited on **Page 5** depend on **Table 6** in the appendix; the T2I-CompBench results are also appendix-only. A main-track paper can use appendices, of course, but the main-paper claims should stand more independently. Right now, several key trust-building components are outsourced to the appendix.

10. **Presentation quality is uneven, with a noticeable number of grammatical issues, imprecise claims, and awkward phrasing that obstruct careful reading.**  
Examples include “we are the first” style claims on **Page 4** without adequate qualification, inconsistent terminology around compactness/length on **Pages 4-6**, and mathematically imprecise wording in several appendix sections. The paper often states strong causal conclusions, such as attributing failures mainly to datasets rather than architecture, without sufficient evidence. This does not make the paper invalid, but it does hurt confidence and makes the argument feel more promotional than analytical.

11. **The annotation analysis is incomplete in a scientifically important way: the paper mostly studies correctness of included labels, not completeness of omitted labels.**  
This is related to Weakness 3, but distinct. The pipeline in **Figure 2** explicitly instructs GPT-4o to identify “as many objects, attributes, and their relations within the image as possible,” yet the validation setup does not convincingly assess whether many valid objects/relations are missed. Since a compositional generation dataset lives or dies by coverage, not just correctness of retained labels, the omission is consequential. A high-precision but low-recall SG can still distort training significantly.

12. **The qualitative evidence is helpful but somewhat curated, and some visual claims are stronger than what the figures clearly establish.**  
In **Figure 5**, some rows indeed support the authors’ claims, but others are less decisive because several competing outputs are blurry or stylistically different, making semantic comparison difficult. Also, **Figure 3** is used to argue that SG annotations are both “more compact” and “significantly longer than sparse text,” which is conceptually muddy. A structured representation can be compact in syntax yet still longer in token count, but the paper does not explain this distinction well, and the figure itself does not settle the issue.

## Questions
1. The most important question concerns evaluation validity. Can the authors provide stronger evidence that the GPT-4/GPT-4o-based SG extraction used for SG-IoU, Entity-IoU, and Relation-IoU is not systematically biased in favor of SG-formatted supervision? For example, what happens on a manually annotated subset, or with a completely different extractor?

2. For the human verification in **Appendix A.5**, please clarify exactly how “Actual Occurrences” in **Equation (3)** are counted. Is this measuring precision of annotated items, recall against all items in the image, or something else? Please provide both false positives and false negatives if possible. This would materially increase my confidence in the dataset quality claims.

3. Please state precisely what parameters are trained for SDXL-SG, SD3.5-SG, and FLUX-SG. Are the base backbones frozen and only the SG encoder learned, or are adapter/cross-attention blocks also optimized? The wording around **Equation (2)** and the fine-tuning description is ambiguous.

4. The paper’s contribution would be easier to assess if the authors explicitly compared LAION-Comp to prior LAION-based structural datasets or annotation pipelines in a dedicated table. Can the authors add a direct differentiation table covering scale, annotation schema, vocabulary, relation types, backbone support, and benchmark protocol?

5. Can the authors provide more details on the graph construction used by the GNN? In particular, how are attributes represented, how are multi-word relations handled in message passing, what is the exact GNN variant, and how are long scene graphs truncated or padded before conditioning the backbone?

6. For **Table 2** and **Table 3**, are the reported improvements averaged over multiple random seeds or a single run? Some of the gains are moderate, and variance would help interpret robustness.

7. Since CompSGen Bench is built from the paper’s own dataset, can the authors strengthen the main-paper evaluation with a more prominent external benchmark analysis rather than leaving it mostly to the appendix?

## Flag For Ethics Review
- Yes, Privacy, security and safety  
- Yes, Legal compliance (e.g., GDPR, copyright, terms of use)  
- Yes, Responsible research practice (e.g., human subjects, data release)  
- Yes, Potentially harmful insights, methodologies and applications

## Details Of Ethics Concerns
The work is based on LAION-Aesthetics / LAION-derived web-scale imagery, and the paper does not meaningfully discuss licensing, copyright status, terms of use, or downstream redistribution constraints for the released annotations and trained models. Since the authors plan to release “annotations with associated processing code, the foundation models and the benchmark protocol” on **Page 3**, legal and responsible-release considerations are relevant.

There is also a modest safety concern around stronger controllable generation and editing interfaces. The appendix explicitly promotes object-level editing and flexible modification via structured graph operations (**Figure 6**, **Figure 7**), which can be beneficial, but also lowers the barrier for manipulating scene content in a precise way. The social impact section acknowledges misuse at a high level, but concrete safeguards are not discussed.

Finally, the user study involves human participants and the appendix states IRB approval, which is good. However, the main paper barely mentions this, and the release plan for derived annotations from web images still deserves clearer documentation.

## Soundness Rating
2: fair. The paper has a plausible technical core and meaningful experiments, but several central claims rely on evaluation pipelines and annotation-validity arguments that are weaker than the paper suggests.

## Presentation Rating
2: fair. The overall structure is serviceable and the figures/tables are useful, but the exposition is uneven, several methodological details are underspecified, and some mathematical/statistical terminology is used imprecisely.

## Contribution Rating
2: fair. Building a large SG-annotated dataset on top of LAION is potentially useful, and the experiments suggest some value, but the paper does not yet differentiate itself sharply enough from related work or support its strongest conclusions convincingly enough for a higher score.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted. The dataset direction is interesting and the empirical signal is nontrivial, but the current version has too many substantive issues around novelty positioning, evaluation validity, annotation verification, and method specification for me to recommend acceptance with confidence.

## Reviewer Confidence
4: confident. I am familiar with the relevant literature on compositional image generation, scene-graph conditioning, and diffusion/flow-based image synthesis, and I carefully checked the main technical and experimental claims, though some implementation details remain unclear from the paper.