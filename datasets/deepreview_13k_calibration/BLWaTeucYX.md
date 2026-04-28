# Generating CAD Code with Vision-Language Models for 3D Designs

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Generative AI has transformed the fields of Design and Manufacturing by providing efficient and automated methods for generating and modifying 3D objects. One approach involves using Large Language Models (LLMs) to generate Computer-Aided Design (CAD) scripting code, which can then be executed to render a 3D object; however, the resulting 3D object may not meet the specified requirements. Testing the correctness of CAD generated code is challenging due to the complexity and structure of 3D objects (e.g., shapes, surfaces, and dimensions) that are not feasible in code. In this paper, we introduce {\ours,} a novel approach to iteratively verify and improve 3D objects generated from CAD code. Our approach works by producing ameliorative feedback by prompting a Vision-Language Model (VLM) to generate and answer a set of validation questions to verify the generated object and prompt the VLM to correct deviations.  To evaluate \ours, we introduce, \emph{CADPrompt}, the first benchmark for CAD code generation, consisting of $200$ natural language prompts paired with expert-annotated scripting code for 3D objects to benchmark progress. Our findings show that {\ours} improves VLM performance by providing visual feedback, enhancing the structure of the 3D objects, and increasing the success rate of the compiled program. When applied to GPT-4, \ours achieved a 7.30\% reduction in Point Cloud distance and a 5.0\% improvement in success rate compared to prior work.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper entitled “GENERATING CAD CODE WITH VISION-LANGUAGE MODELS FOR 3D DESIGNS” proposes an approach to generate and verify CAD 3D objects from natural language. The proposed approach introduces a verification step called CADCodeVerify. CADCodeVerify use Vison Language Machine (VLM) to verify CAD objects against generated visual questions. The hypothesis is that the question serves as visual properties the object should satisfy to meet the structural specification. The key contribution of this approach is the use of a refinement step. From the language prompt that describes the object in natural language, a first CAD description code (CADQuery) is generated. The visual questions are also generated from this language prompt input. The object (CADQuery) is verified against visual properties questions using a VLM that generates feedback for each questions. This feedback is used to refined the CADQuery code.

To summarise, the contributions of this work is two fold: 1) an automated CAD generation approach that does not necessitate humain interaction; 2) a dataset called CADPrompt that comprises 200 CAD objects. Expermental results shows when implemented using GPT-4 LLM, we observe improvements in object generation accuracy and an increased success rate compared to other LLMs.

### Strengths
- Novelty and Originality: The integration of question/answering based VLM to refine the object quality. 

- Evaluation: The increase of success rate of compilable outputs at the end of the refinement shows that the method can improve the generation of CAD code from language prompt.

- Soundness: The technical approach is sound and could be applied to a lot of CAD or CAV tasks. The approach is a specification refinement method using generative AI. From an initial specification, an initial object plus query are generated. Then, feedback from query satisfaction are used to improve the object. A dataset is provided and metrics are determined to rank the quality of the generated object. This has applications beyond CAD specifically.

### Weaknesses
 - Dataset Scope: CADPrompt could have been better introduce, showing the most complex objects in terms of complexity and difficulty metrics. 

- Complexity Metric for Objects: This paper measures object complexity by counting vertices and faces. However, using metrics like bounding boxes or decomposed bounding volumes could better reflect structural complexity. Vertices mainly define shape details, not true complexity—a simple shape like a cube can have many polygons, while complex shapes like an aircraft wing might need fewer. In physics engines, object complexity is often defined by the volume structure the object requires. Lower polygons can shape more complex structures.

- Difficulty Metric for Objects: The current method of measuring complexity through word and line count for the natural language descriptions and Python code may not fully capture their complexity. A semantic-based complexity metric, where each instruction has a complexity value, would better reflect how nuanced or contextually challenging the description and code are, which could impact model performance.

- Clarity and Readability: Certain sections are overly technical and hard to understand without referencing the appendix. Simplifying these sections would improve accessibility for readers. Terminological inconsistencies between LLM used for language to code and code with feedback to code and VLM for image and questions to answers also introduce potential confusion, which could be resolved for clarity. Certain sections are overly technical and hard to understand without referencing the appendix. Simplifying these sections could enhance accessibility for readers. For example, consider moving equations 1-7, which aren't essential for understanding the main contributions, to the appendix. Conversely, evaluation metric equations (8-10), such as those for point cloud distances, Hausdorff distance, and IoGT, should remain in the main text. Additionally, bringing valuable visuals currently in the appendix (Figures 5, 11, 12, and 14) into the main text would ease the understanding and improve work illustration. The paper would also benefit from a stronger focus on scientific insights and hypothesis testing over too much detailled descriptions. For instance, providing context around why a fixed number of five verification questions is used, without adapting to object complexity, would clarify the rationale. Similarly, explaining why only two refinement iterations are applied, regardless of complexity, would better illustrate the scientific intuitions driving these choices. Furthermore, details on how AI context like 7, 9, and 10, have been engineered such as crafted based on expert knowledge or through authors tuning would be valuable. Shifting focus to the "why" rather than the "what" would help readers grasp the paper challenges.

- Positioning: the paper’s positioning within the state of the art could be made clearer, with more explicit distinctions from existing work. The paper integrates the related work 3D-premise in the experiments, but didn't explicitly state the approach difference. The feedback is based on question answering rather than the initial description of the object.

### Questions
- Q1: I appreciate the framework’s contribution, but could you provide a bit more on how this specifically differs from or builds upon prior work (3D-Premise)? Is it an improvement or an entire new approach?

- Q2: Can you tell us more about the quality and diversity of the CADPrompt dataset? I’m curious about how it’s tailored to the goals of your approach. A bit more on why it’s a good benchmark—perhaps a breakdown of object types, complexity levels, or any specific challenges it presents?

- Q3: The experimental results look interesting, but it would be good to understand more in details where the approach performs well and where it might have limitations. Do you have any insight to share about this?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces CADCodeVerify, a approach to iteratively verify and improve 3D objects generated from CAD code using Vision-Language Models (VLMs).  The method involves generating CAD scripting code from natural language prompts, executing the code to render a 3D object, and refining the code based on visual feedback through a question generation and answering process, to correct deviations from the initial specifications.  The approach is evaluated using CADPrompt, a benchmark dataset of 200 3D objects with corresponding natural language prompts and expert-annotated code.  The approach is evaluated on GPT-4, Gemini 1.5 Pro and CodeLLama models.

### Strengths
-	The paper comes with a new benchmark suite (CADPrompt) which is a well-curated, crowd-sourced benchmark with annotations and quality checks, which is a valuable resource for assessing CAD code generation and refinement methods.
-	CADCodeVerify uses an interesting novel idea to eliminate the need for human involvement by generating validation questions and answering them using VLMs.
-	The geometric solver-based baseline is very interesting and gives an upper estimate of the self-refinement process; it would be interesting to explore if this solver could also be used as a metric for evaluation.

### Weaknesses
-	The fundamental differences between CADCodeVerify and 3D-Premise are unclear. For example, it’s not specified whether 3D-Premise uses execution-error-based repair. Also, both approaches seem to use totally different prompts, so it is not clear if it is just a matter of better prompting or something fundamental (such as the question-answer based method)
-	The paper would be stronger if the approach was also evaluated on the 3D premise dataset
-	Some other details are missing (see below questions) regarding ambiguity in NL input and chain-of-thought based extension to 3D-Premise.



### Questions
1. Would providing images of the generated object from multiple viewpoints improve 3D-Premise’s performance? What about using a chain of thought prompting (for e.g. explicitly ask the model to reason whether each criterion in the initial task are satisfied)? This will be similar to CADCodeVerify, but doing 1 VLM call instead of doing 3 VLM calls in the verify step  to reduce the inference time. 

2. In Figure 3, does 3D-Premise also repair code based on compile error messages?

3. How do you handle ambiguity in inputs in ground truth solutions? For example, if the NL input does not specify a particular size of hole, there could be many ground truth solutions which might impact the cloud-distance based metrics. 

4. Since Point Cloud distance and Hausdorff distance are noisy metrics, how does the generated CAD program compare on the geometric metrics obtained using the geometric solver?

Minor: 
- Consider renaming success rates to compile rates or something similar to convey that is only compilation success rate and not overall task success rate. 

- For figures 5,6 (running examples), it will be useful to also see the repair steps.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work contributes a new method for VLM-based CAD code synthesis, and a new dataset for evaluating CAD programming models. It builds on past work on code repair for CAD synthesis – the core idea is that instead of just providing the current render during repair (as prior work 3D-Premise did), the LLM also comes up with *verification questions* based on the task description (not using the current render) which it then answers (using the current render). These Q/A pairs are summarized into feedback for what needs changing, which is provided to the repair model alongside the current render to prompt code repair.

The dataset, CADPrompt, was constructed by selecting objects from a dataset used in prior work and annotating them with language prompts along with Python CAD code. They evaluate on a range of models (GPT4, Gemini, CodeLLama) and compare to several baselines (no refinement, 3D-Premise, and Geometric Solver). The last of these baselines, Geometric Solver, is also a contribution – it's a baseline that gets to "cheat" and compare the ground truth model to the current rendered model in terms of a range of geometric feaures. Their methods generally outperforms the baselines.

### Strengths
- The contribution of a language-to-CAD dataset is useful for the community, and hiring CAD experts to write the CAD code for it means it's likely high quality.
- The comparison is run across a range of LLMs including open source ones (CodeLlama) 
- They generally surpass the 3D-Premise baseline and score fairly close to the geometric solver baseline that gets to cheat and use the ground truth CAD model in calculating its feedback. They score particularly well on the more difficult problems, and benefit more from feedback than 3D-Premise. They show improvement across three different similarity metrics in addition to compilation success rate.

### Weaknesses
 - The term "success rate" is a bit of a misleading name for something that means "compilation rate" or "compilation success rate" – it gives me the impression that the model succeeded at solving the task, not that it generated an arbitrary piece of code that compiled. For example in the abstract "increasing the success rate of the compiled program" or in the intro "5.5% increase in successful object generation" all gave me this impression until I dug into it.
    - Also, the abstract says 5.0% and the intro says 5.5% – which is correct?
- Does 3D-Premise get to do the Code Execution step described in 3.2, where if compilation fails it retries with compiler feedback up to N times? If not, it seems important to do this comparison to disentangle how much of the benefit is coming from compiler feedback versus the Q/A contribution.
- The improvements are modest but still reasonable – I would defer to a reviewer more familiar with these metrics on this. Looking at GPT-4 Few-shot in Table 2 (which looks like overall the best model), the IoGT metric difference is .942 vs .944, the Point Cloud distance is .127 vs .137, and the Hausdorff distance is .446 vs .419. These are not huge differences, but still a notable step towards the Geometric Solver performance.
- It's confusing that "Refine 1" causes 3D-Premise to decrease in performance in Figure 3 – see full note in "Questions" section, but clarification on this would be helpful to understanding the results.

### Questions
- Is the Geometric Solver output given to an LLM during the feedback phase? I assume so given how it varies depending on which LLM is used in Table 2. Does it get to do two rounds of feedback like the CADCodeVerify model does?
- "Refine 1", "Refine 2", and "Generated" should be defined somewhere, right now the first place they appear is in Figure 2 headings (which are not searchable text in the PDF) and then when discussing results, but they aren't clearly defined.
    - Is "Generated" the step right after Section 3.1 finishes or right after Section 3.2 finishes – i.e. is "Generated" before or after the compiler-error based verification step?
    - Are "Refine-1" and "Refine-2" the two rounds of refinement (Section 3.3) or is the first one the code repair from Section 3.2?
- Why does "Refine-1" go *down* so much in Figure 3 for 3D-Premise? This is very surprising to me and would be helpful to clarify. Refinement ought to help, and it did help them in that prior work. While it's not as strong of an effect, refinement also seems to hurt all the methods a bit in some of the other plots (like the Complex plot) – why would rounds of refinement hurt instead of help?
    - These graphs are showing the compilation rate. It'd be helpful to see changes in the other metrics from Table 2 that have to do with correctness instead of whether or not the code compiles – those seem key to understanding whether feedback is helping.

Minor fixes:
- The CADQuery compiler $\phi$ is deterministic, right? So the "$\sim$" should be an "=" on line 177
- The description of the "number of compilable outputs" discussed in 305-310 was confusing to me until I saw the caption of Figure 11 in the appendix. It would be helpful to move part of this description to the main paper – it wasn't clear to me that this meant the number of experiments where the code compiled successfully. And to clarify – are those 6 experiments the six large rows in Table 2 (that vary between language model used and not between method used)?
- In discussing the geometric solver the paper notes "This feedback method serves as an upper limit for CAD code refinement, as it conveys the precise geometric differences between the generated 3D object and the ground truth." While I think this is a useful baseline, it's not literally an upper limit for performance from code refinement feedback – as shown for example by how it's occasionally outperformed in the experiments. It's a great baseline to have, I just would suggest against using the term "upper limit" for something that's not actually an upper bound.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a technique called CADCodeVerify that uses feedback generated from VLMs to refine CAD code generated by LLMs in an iterative manner. This is a novel technique proposed to address a reasonably difficult and seemingly important problem. The paper evaluates this technique against an existing baseline called 3D-Premise and also with a baseline using feedback from a geometric solver. CADCodeVerify shows better performance against both baselines.

### Strengths
This paper is written really well. As someone who doesn't work much with CAD code, it was immediately clear what the limitations were and how they intended to address them. The technique itself is novel for the application and is well described with appropriate examples. I also appreciate the effort taken for creating the benchmark tasks over which the systems were evaluated.

### Weaknesses
One main weakness I can see is the lack of baselines. However, this is not a major issue to me since I don't know of other systems that target this specific problem. However, I can think of other techniques like chain of thought prompting, or techniques using some form of reasoning, against which we can compare CADCodeVerify. Right now, the only true baseline seems to be 3D-Premise, and another baseline that uses an alternate form of feedback generation, though I could be mistaken here.

### Questions
1. In Fig 1, within the CADCodeVerify block, I see step 3.c generating feedback which then produces a new object. My question is: what exactly is the input to the VLLM? Is it the feedback, that then generates the code that compiles to produce the new object, or is it the new object itself? I suspect it is the former, but the figure indicates it to be the latter.
2. In the evaluation, do you consider naive or basic prompting? For example, just a zero-shot or few-shot prompt to an LLM that produces code? Is that what the "Generated" field in Table 2 is?
3. Are there any insights as to why CADCodeVerify performs better than baselines? For instance, what is it in the proposed technique that allows it to outperform 3D-premise? And why is VLLM feedback more useful than geometric feedback, even when the latter needs the presence of ground truths? One would imagine a technique needing GT labels for providing feedback would be more accurate or equivalent to a technique operating without the labels.
4. Maybe I missed this in the text, but in Fig 3, what is Refine 1 and Refine 2?
5. Are there any limitations as to the complexity and difficulty of the benchmark tasks? I understand they vary in complexity and difficulty, but at the same time CADCodeVerify does quite well, even reaching around 90% accuracy in the hardest case. Is there a class of problems this benchmark is not testing, or are the hard problems simply not hard enough?
6. How representative is the benchmark of the objects actually being drawn in the industry today? One major challenge with code generation has always been that it has never been representative of IRL code. Do we see the same challenges here?
7. What dataset was 3D-Premise originally evaluated on, and why have you not evaluated CADCodeVerify over that? What is different about your dataset that sets it apart from the one 3D-Premise used?

### Soundness
4

### Presentation
4

### Contribution
3
