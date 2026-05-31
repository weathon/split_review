## Human Reviewer 1

### Summary
This paper proposes a new metric, LEGO-Eval, for evaluating the 3D embodied environments.  LEGO-Eval uses multiple tools to extract the information from the scene and verify if they satisfy the constraints. The evaluation results demonstrate LEGO-Eval achieves much higher agreement with human judger than previous metrics like CLIP-Score.

### Strengths
1. The proposed metric has much better agreement with human judgement compared to other metrics.
2. The refinement experiments is a highlight that such metrics can be reliable rewards for improving systems.

### Weaknesses
**Require dense scene annotations.** This is the major concern of the proposed evaluation metric which requires dense annotations of each assets (attributes, locations, etc). However, for some methods which generate entire scene in a single mesh (e.g., diffusion-based model), the proposed method cannot use tools to get those information. The results in Table 2 also validate this concern that, with textual reasoning on attributes and precise spatial information from rendering engine, the performance will drop significantly. Therefore, the usability of the proposed metric is quite limited.

### Questions
1. How many human annotators are recruited for collecting human judgments?
2. How many examples are used in Figure 7 to get the results?

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper tackles a pain point in text-guided 3D scene generation: we can now generate scenes from language, but we can't reliably tell if the scene actually matches the detailed instruction. Existing automatic evaluators (e.g., CLIPScore) don't really understand 3D layouts, and they crumble on constraints.

To address this, the authors propose LEGO-EVAL, a tool-augmented evaluation pipeline. The idea is: Take the long instruction, identify and break it into structured constraints (4 types so far); For each constraint, plan which tools to call (Unity environment interaction, textual reasoning, VLM reasoning), execute those tools to actually ground the entities, and then give a binary judgment with evaluation explanations, declare the whole scene valid only if all constraints pass.

Alongside this, the authors build LEGO-BENCH, focusing on the attributes and spatial relationships of 3D scene generations, so that different evaluators can be compared.

### Strengths
- Reframes 3D-scene evaluation as a tool-augmented reasoning task. Combining constraint extraction, planning, and multimodal tool calls for grounding is a novel and well-motivated contribution.
- The pipeline and tool taxonomy are well-explained. Figures and examples make the method intuitive.
- Strong experiments with fair baselines (e.g., CLIPScore, SceneEval). Clear metrics, ablations, and human alignment analyses.

### Weaknesses
- Simulator dependency: LEGO-EVAL assumes access to the scene graph and Unity backend. This may not be available in many real settings like photorealistic assets.
- Scene limination: LEGO-BENCH is limited to indoor scenes. Broader or more varied data would strengthen claims.
- Failure analysis: It's unclear which constraint types cause most errors for baselines.

### Questions
1. Can LEGO-EVAL operate without simulator access?
2. What is the average tool-call cost per instruction and runtime per scene?

### Soundness
3

### Presentation
3

### Contribution
4

### Rating
6

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper builds on the core insight that existing evaluation methods (such as using VLMs as judges) do not adequately match fine-grained text instructions with 3D scenes; this becomes a problem for downstream use-cases such as text-to-scene synthesis. To address this, the paper introduces (i) LEGO-Bench, a manually annotated (n = 130) dataset of text-scene pairs, and (ii) LEGO-Eval, a tool-based evaluation method that drastically outperforms VLM-as-judges when compared to ground-truth.

### Strengths
1. LEGO-Eval’s tool-grounded pipeline drives a striking jump in F1 versus the usual VLM-as-judge baselines, showing that explicit grounding leads to better alignment verdicts.

1. LEGO-Bench is valuable: 130 instructions with roughly 1.2k hand-checked constraints covering both architectural makeup and object relations give the community a realistic, fine-grained stress test. The field of scene graphs, while tangential to this paper, _also_ incidentally lacks high-quality fine-grained annotations for scenes, despite it being a common drawback of VLMs. 

1. The paper is well-written and easy to follow. The experimental coverage is thoughtful; it has ablations over tool types, comparisons against four synthesis systems, and the Holodeck refinement loop (Fig. 7) all help illustrate the usefulness of LEGO-Eval/Bench.

### Weaknesses
1. The paper does not provide conclusive evidence (or even a brief discussion) to the claim that finer-grained text-scene alignment leads to real embodied gains. The paper does provide _preliminary_ evidence via the Holodeck refinement vignette (Fig. 7); however there’s no “detect -> repair -> retrain” loop or even a pointer to existing sim-to-real failures. A minimal downstream study (or stronger citations) would make the story much more convincing.


1. LEGO-Eval leans on several Unity-facing tools, so the comparison to image-only VLM judges risks being apples-to-oranges. Please add baselines that ingest similar structure (e.g., VLM + detector/scene-graph outputs, see weakness #2 and question #3 below) to show the lift truly comes from the proposed orchestration.


3. The paper has a limited analysis of failure modes of VLM-as-judges. Figure 8 hints that VLM judges mostly hallucinate or misidentify objects, yet we never see how often that happens or how severe it is. Please tally the dominant error types (mis-identification, spatial mistakes, attribute mismatches) so we can tell whether cascading failures are the main culprit. If mis-identification dominates, test baselines that feed object detection outputs [1,2] or structured summaries from scene graph generators to see how much ground they recover. Likewise, benchmark 3D-language models (3D-LLM, Point-LLM) that already encode volumetric context. A quantitative breakdown plus these stronger baselines would clarify when LEGO-Eval is indispensable versus when richer perception priors nearly match it.

[1] Grounding-DINO. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. https://arxiv.org/abs/2303.05499
[2] YoloV8, https://yolov8.com/

### Questions
1. As mentioned above, do you have any downstream evidence (even a small detect -> repair -> retrain study, or at least documented cases in the literature) that tighter instruction-scene alignment boosts embodied performance?

1. Can you quantify the cost tradeoff of LEGO-Eval: number of tool calls per instruction, duration (limitation currently mentions "two hours" for the 260 samples), and approximate compute cost per sample. How do these figures compare to the single-pass VLM judge?

1. It seems that LEGO-Eval is specifically targeted at static, top-down scenes and requires careful tool curation. Can it theoretically cope with dynamic scenes? Furthermore, would it make sense to add scene graph generators [1,2], which produce fine-grained annotations from scenes, as a possible baseline? 

I am quite willing to raise my score if the above questions and weaknesses are addressed.

[1] Gu et al, ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning. https://arxiv.org/abs/2309.16650
[2] Huang et al, LASER: A Neuro-Symbolic Framework for Learning Spatial-Temporal Scene Graphs with Weak Supervision. https://arxiv.org/abs/2304.07647

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper introduces LEGO-EVAL, a new evaluation framework that uses a diverse set of tools (for environment interaction, textual reasoning, and multimodal reasoning). This tool-augmented approach allows it to explicitly ground scene components and accurately assess if the generated 3D scene aligns with complex, detailed instructions. 

The authors also created LEGO-BENCH, a new benchmark of fine-grained instructions for 3D environments. Experiments show LEGO-EVAL dramatically outperforms VLM-as-a-judge (0.81 vs. 0.40 F1 score) in alignment with human judgments.

### Strengths
Instead of relying on one AI model to just "look" at the scene, the paper introduces LEGO-EVAL, which acts more like a detective. It uses a set of specialized "tools" to check specific facts—one tool to find all the objects, another to check their color, and another to measure their spatial relationships.

The authors created their own difficult test (called LEGO-BENCH) full of complex instructions. They proved their new "judge" (LEGO-EVAL) is far more accurate than older methods.

Experiments also show that current AI models for building 3D scenes are still very bad at following detailed instructions, failing most of the time.

### Weaknesses
The paper introduces a new test set called LEGO-BENCH, but it only contains 130 instructions. This is a very small number, which might not be enough to prove the necessity of making such a benchmark. In fact, there are many indoor scene synthesis benchmarks and it is not even worthwhile to start a new language-instructure synthesis from scratch.

In LEGO-BENCH, the scenes used to test the evaluator were created "manually." This process is very slow, expensive, and hard to scale. Utilizing a sequence call of LLM APIs to generate, verify, and refine, seemed to be costly and super inefficient in generating a simple contraints scene from natural language.

The best results come from using "GPT-4.1." The paper shows that performance drops significantly when using smaller or different models. This means the system's success isn't just its smart design but also its reliance on a very powerful (and expensive) "brain" that not everyone can access or afford. For example, does a 7B or 4B model good enough to generate good results based on the method proposed?

Considering the downstream tasks, what can this method bring advantages to? e.g. robotic learning? navigation? gaming?  The dataset from "manually collect instructions for 3D scene synthesis" may not be super useful for other envs, tasks, game engines, simulations, e.t.c. In another language, the impact of this LEGO-BENCH is too small.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
2

### Confidence
4