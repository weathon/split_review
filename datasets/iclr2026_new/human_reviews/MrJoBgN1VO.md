## Human Reviewer 1

### Summary
How well can models engage in geometric reasoning? How well can models engage jointly over structured symbolic and spatial representations? The authors formalize a new evaluation task (Program-to-Geometry), collate a new testbed for this task, and apply that testbed to assess current models.

### Strengths
The paper is well-motivated and engages with an interesting reasoning challenge (understanding geometric reasoning as it relates to symbolic representations of those problems). The authors' benchmark is quite well-structured in my opinion --- particularly in having multiple difficulty levels and coding by concept. That kind of granular decomposition will surely help other researchers and model developers better isolate and probe model capacities! 

I also appreciated the diversity of model analyses the authors engaged in (both quantitative and more qualitative, e.g., Section 6). 

I also found the authors' formalization and explication of two kinds of answer leakage very important and a valuable contribution in its own right!

### Weaknesses
While the empirical work is wide-ranging, I think the paper could be improved in clarity and rigour of the empirical analyses. For instance, the authors sample with a moderately high temp (0.6), to my understanding. However, no error bars are reported? How variable are the results? It would be good for the authors to present some sense of performance variation across tasks (e.g., 95% CIs around the mean; stdev, etc). 

I also found the phrasing of Program-to-Geometry in Section 3.1 somewhat confusing. It seems like there are two capabilities the authors are interested in (as they lay out in that 3.1). But is Program-to-Geometry as a task both? Just one? It's worth clarifying (and I found that confusing...) 

It also would be good for the authors to clarify how their work relates to https://arxiv.org/pdf/2408.08313, which seems quite similar, especially related to RQ1 (which was at ICLR last year and is not cited).

### Questions
- How much variance is there in model performance (see question above, re: error bars)? 
- For future work, not this revision :) have the authors looked at reasoning token usage across the difficulty levels in the benchmark?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 2

### Summary
This paper introduces GeoGramBench, a benchmark to evaluate large language models' ability to perform geometric spatial reasoning from procedural drawing code (e.g., Asymptote), formalizing it as the Program-to-Geometry task. It highlights LLMs' underexplored weaknesses in translating symbolic code into spatial representations. The benchmark comprises 500 curated geometry problems, organized by a novel three-level taxonomy based on geometric complexity (Primitive Recognition, Local Relation Composition, Global Abstract Integration). Drawing from sources like NuminaMath and MATH-500, the dataset addresses challenges like answer leakage through human refinement and decontamination. Evaluations on 17 frontier LLMs are comprehensive and do reveal the persistent deficiencies.

### Strengths
- The authors effectively address prevalent issues in similar datasets, such as answer leakage, through meticulous processing techniques that significantly elevate the benchmark's overall quality.
- The evaluation spans 17 open- and closed-source models of varying scales, uncovering both the capabilities and shortcomings of existing LLMs in this domain.
- The paper is generally well-written, with smooth and coherent flow throughout.

### Weaknesses
- It would be valuable to incorporate evaluations using vision models that directly interpret the rendered images, alongside results from multimodal models, to serve as a reference baseline. This would help disentangle whether the observed performance gaps arise from deficiencies in reasoning capabilities or challenges in parsing Asymptote code.
- There is a discrepancy between Table 1 and the corresponding text on page 8: "For example, GPT-o1 drops from 76.02% to 43.35%, and DeepSeek-R1 drops from 75.27% to 40.38%." Please verify and ensure alignment between the visual and textual elements.
- The paper would benefit from a standardized definition of the dataset's input-output format, including an accessible, introductory explanation of Asymptote code to enhance clarity for readers unfamiliar with procedural drawing languages.

### Questions
- Could the paper include a formal definition of "Asymptote code" to provide clarity for readers? Additionally, it would be helpful to elaborate on the process of standardizing procedural code from diverse data sources into a consistent format.
- Although benchmarks in this niche are scarce, it would strengthen the discussion to explicitly compare the proposed work with related efforts, such as [1].

[1] Qiu Z, Liu W, Feng H, et al. Can large language models understand symbolic graphics programs?

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
The authors of this paper formalizes this novel task called Program-to-Geometry, which tests the model's abilities make geometric reasoning based on programmatic drawing code. The proposed GeoGramBench, consists of 500 curated problems incorporating programmatic drawing code and evaluated the performance of the 17 current state-of-the-art models on their proposed benchmark.

### Strengths
- interesting insights have been provided in the section 6 "behavior analysis of LLMs"
- detailed description of the data curation process (pre-selection, deduplication, human verification and answer leakage prevention)

### Weaknesses
- a more detailed analysis for the main results table in Section 5.3 is required, it is interesting that they struggle with angle and volumne, but lacks a bit of insights (for example why is this not the most challenging questions for abstract?)
- I am not entirely sure when the experiments have been drafted, but maybe add one most recent model for evaluation?
- The tasks seems undoubtly interesting, and one could see the implication, but testing the model to make geometric reasoning based on procedural code (albeit might have different syntax, but the geometric properties of these DSL are similar, information about the 2D/3D properties are stored somewhere in the code) has been studied for example in SGPBench (similar to the tested ability b in section 3.1 to make spatial and geometric reasoing) and SGP-GenBench (similar to ability a in section 3.1 generate geometric diagrams) and other similar works, in fact a lot of works has been dedicated for that, I would want to have some discussions with benchmarks from that area in the discussion / related work sections
- in general I am open for discussion and modification of my ratings

### Questions
- benchmark is important and interesting for the community to push the boundary of current AI systems, but there are many capabilities that we could that test, the more interesting problems are what are the implications of this benchmark? how can we use this benchmark to improve the current models? if we find a way to improve the models to be better in the proposed benchmarks, are they domain-specific capabilities or can they benefit other reasoning abilities? 
- the authors seem to be discovering that the CoT might not be beneficial for this task, which is fine per se, however, since CoT or different variants are standard approaches for improving the reasoning performance, why does it fail on GeoGramBench? might it be an indication that the tested Program-to-Geometry ability to be a very specific and not generic ability?
- what does the level 1-5 in Figure 2 mean?
- I am a bit confused with figure 1: math-500 and aime 24 are text-only benchmarks, where you getting the visualizations? let's say you constructed it, but you are suggesting in this diagram, that by providing additional visualization to the already existing text and code for geometric shapes, the performance actually gets worse?

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper formalizes Program‑to‑Geometry: reading procedural drawing code (Asymptote/Matplotlib‑style) and performing downstream geometric reasoning. It releases GeoGramBench, 500 curated problems with a three‑level taxonomy 1)Primitive Recognition, 2) Local Relation Composition, and 3) Global Abstract Integration, organized by geometric complexity rather than typical “reasoning complexity,” plus six subtypes from "Angle", to "Count". Across 17 models, accuracy drops sharply at the highest abstraction level, with no model exceeding ~50% there.

### Strengths
1. Code-based spatial reasoning is an interesting and under-explored domain.
2. Clear task definition and a taxonomy grounded in geometric (not step-count) complexity; the benchmark isolates program-to-diagram understanding from general math difficulty. 
3. Broad evaluation over 17 models with consistent prompting and multi-sample reporting; the “<50% on Abstract” result is a useful negative finding that signals a genuine capability gap.
4. The ANSWER LEAKAGE CHALLENGES is sound and interesting.

### Weaknesses
1. Positioning vs. prior art (major). The paper does not cite SGP-Bench (ICLR 2025), which evaluates LLMs’ understanding of symbolic graphics programs without rendering as well, at broader scope (SVG for 2D; CAD for 2D/3D) and with systematic invariance tests under program transformations. While GeoGram focuses more on the 2D geometry math aspect, I think SGP-Bench is closely related and predates this submission, it should be discussed and contrasted.
2. GeoGramBench stays within Asymptote/Matplotlib-style code and contest-style numeric targets. That makes results crisp, but limits to the mathematical geometry domain which is a fraction within the broad discussion of geometric spatial capability.
3. While the paper's goal is to evaluate the program-to-geometry / geo-spatial capability of the LLMs, the questions also involve mathematic reasoning capability to solve the planar geometry tasks. Therefore, the final accuracy is kind of inconclusive for the geo-spatial one itself.
4. I think the DSL choice (Asymptote/Matplotlib‑style) can significant affect the evaluation results since various LLMs could be exposed to different amount of DSL code training. few-shot CoT experiments are important to justify the evaluation.

### Questions
I would like know the authors' thoughts and opinions regarding the weaknesses section.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
4