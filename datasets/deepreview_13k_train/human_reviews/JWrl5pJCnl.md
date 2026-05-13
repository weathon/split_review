# Instruct2Act: Mapping Multi-modality Instructions to Robotic Arm Actions with Large Language Model

- Decision: Reject
- Scores: 6, 3, 6, 5

## Abstract
Foundation models have made significant strides in various applications, including text-to-image generation, panoptic segmentation, and natural language processing. This paper presents \texttt{Instruct2Act}, a framework that utilizes Large Language Models to map multi-modal instructions to sequential actions for robotic manipulation tasks. Specifically, \texttt{Instruct2Act} employs the LLM model to generate Python programs that constitute a comprehensive perception, planning, and action loop for robotic tasks. In the perception section, pre-defined APIs are used to access multiple foundation models where the Segment Anything Model (SAM) accurately locates candidate objects, and CLIP classifies them. In this way, the framework leverages the expertise of foundation models and robotic abilities to convert complex high-level instructions into precise policy codes. Our approach is adjustable and flexible in accommodating various instruction modalities and input types and catering to specific task demands. We validated the practicality and efficiency of our approach by assessing it on robotic tasks in different scenarios within tabletop manipulation domains. Furthermore, our zero-shot method outperformed many state-of-the-art learning-based policies in several tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper looks at the problem of generating control programs for robotic control with the help of foundation models. Part of the functionality that can be leveraged in the program are based on visual (SAM) and visual-language (CLIP) foundation models. The programs themselves are obtained by prompting an LLM. The prompt is equipped with external libraries, function descriptions and example programs. The method is tested on benchmarks with text only instructions as well as text-visual instructions and performs competitively. Extensive ablation studies show the importance of individual elements of the prompt and how the choice of foundation models impacts performance. The model shows OOD capabilities, that cannot be achieved by prior methods.

### Strengths
- Extensive ablation studies that showcase specific abilities of the model (types of OOD generalization), investigate the role of the foundation models and study the importance of the components of the prompt. 

- Removing the dependence of engineered perceptual models from the CaP method by using foundation models.

- Slight improvements over CaP via the different prompting method.

- The methods and results are presented in an understandable manner.

### Weaknesses
 - Standard Errors: The VIMABench experiments were run over three random seeds for each meta-task but results are reported without any standard errors? In case of the textual prompts benchmarks its also not clear to me why no standard errors on results are reported?

- Choice of baselines: For the VIMABench I find the choice of baselines not insightful. On the one hand the baselines make use of a large set of training trajectories, but on the other hand these methods train policies that choose low-level actions. The presented method chooses action primitives such as "PickAndPlace" but does not need much training data (apart from the examples). I think adapting CaP to the VIMA benchmark would be a more insightful baseline. 

- I think it makes sense in the comparison with CaP to compare using an oracle object detector, but one of the main novelties of the work is replacing the perceptual modules of CaP with foundation models. Therefore it would be interesting to see how this affects performance, i.e. just run the method on the CaP benchmark without the oracle.

- Too much detail in related work: I think the related work section is too long and just a list of papers rather than helping to place the work in the research area. I would shorten it and move interesting results from the Appendix to the main paper.

### Questions
- Paragraph 4.4: What does RR stand for? 

- Are the example programs in the prompt fixed for every task or do they depend on the task ?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The proposed methodology introduces a way to utilize existing off-the-shelf vision and language foundation models for solving robotic tasks. The framework can be conditioned on language and or visual input, and produces Python programs for completing the given task. Experiments in both simulation and the real world demonstrate that the proposed system can outperform baselines.

### Strengths
- Well-written. The paper is very well-written and easy to follow. The figures very much aid in understanding the paper.
- Ablations. Ablations are conducted to better understand various design choices of the proposed methodology.

### Weaknesses
 - Unfair comparison to baselines.
  - CaP
    - The proposed work's claimed distinction with CaP is unclear. The authors write "Unlike existing methods such as CaP (Liang et al., 2022), which directly generates policy codes, our approach generates decision-making actions that can help reduce the error rate when performing complex tasks." But, the proposed methodology also uses LLMs to generate Python programs, so the distinction is unclear. Furthermore, about CaP, the authors write: "However, its capabilities are limited to what the perception APIs can provide, and it struggles with interpreting longer and more complex commands due to the high precision requirements of the code." This seems to be a limitation of the proposed methodology as well, which also relies on a finite number of available APIs. Hence, again, the distinction between the proposed methodology and CaP is unclear.
    - Why is the oracle version of the proposed method used when comparing to CaP, instead of the non-oracle method? This seems to be an unfair comparison.
    - Even then, the performance gap seems trivial. Is there any evidence to suggest that the gap in performance is non-trivial?
  - PerAct
    - The authors write: "For simple 3D tasks, such as stacking objects, we introduced an additional parameter to indicate the current occupancy. For more complex tasks, such as opening a drawer, we added some heuristic movements to ease the execution." PerAct was able to operate without such simplifying assumptions, which makes this comparison unfair. 
    - Even then, the performance gap is very small. How do we know this is a non-trivial gap in performance? Is there a trend of tasks / cases where the proposed methodology succeeds and PerAct fails? What is the intuition behind the proposed methodology outperforming PerAct, which was trained directly for the task at hand? 
  - Decision Transformer
    - How was comparison to DT done, as DT doesn't take in language instructions?
    - What is the intuition behind the page gap in performance between the proposed methodology and DT?
- Simplistic Tasks.
  - The tasks considered for evaluation seem limited in complexity, e.g. are simply pick-and-place like tasks. These are tasks which can be very easily solved. More complex tasks have not been explored.
  - Furthermore, as the "Generated Policy Code" in Figure 3 depicts, there is an API for pick-and-place, which the system simply calls upon. This simplifies the already simple problem quite a bit, by abstracting away the more difficult low-level control.
  - Finally, a lot of processing / engineering is done to get the system to work (e.g. applying a gray threshold filter followed by a morphological closing operation, a morphological opening operation, Non-Maximum Suppression, etc.). If all of this engineering was required to get a simple task like pick-and-place to work (which is further simplified with the use of a pick-and-place API), then I find it difficult to see how the proposed methodology could be extended to more complex manipulation tasks, thereby limiting its utility.

### Questions
- "Although the language models may occasionally generate incomplete or incorrect code, such as missing brackets, punctuation, or mismatched cases, the Python Interpreter can detect these errors and prompt us to generate new code."
  - What is done in these situations? Is the LLM simply prompted a second time, with the hope that the output will not contain incomplete or incorrect code?
- How much prompt engineering went into this when evaluation? Were the prompts the same across tasks, and across methods (ie when comparing to the baselines)?
- How computationally expensive / slow is the framework? Can the tasks be solved in real-time?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents Instruct2Act, a framework that leverages Large Language Models (LLMs) to convert multi-modal instructions to sequential actions for robotic manipulation tasks. It uses pre-defined APIs to access multiple foundation models. Its approach is validated in both simulation and real-world experiments.

### Strengths
1. Instuct2Act represents a whole pipeline from utilizing multimodal instructions to actions. This is meaningful in embodied ai domain.

2. It can handle a diverse range of task types.

3. This paper includes suckers and gripper in simulations, and conducts real-world experiments.

### Weaknesses
1.	The embodied ai plus LLM develops too fast. It seems that this paper a little bit lacks of novelty. Instruct2Act seems like the combination of VIMA and CaP.


### Questions
1.	I think the author should add GPT-4 api and Codellama in ablation? 

2.  What’s the main improvement of Instruct2act? Could the authors list some difference between Instruct2act and VIMA, except for using foundation model to detect the objects?

3.	For the franka manipulation, as the paper mentioned: 'Our method is presently limited by the basic action primitives, such as Pick and Place.' So, the franka-based tasks also uses the action primitives?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This study targets the challenge of robotic manipulation tasks utilizing a Large Language Model (LLM) guided by multi-modal instructions. The efficacy of this approach has been tested with various instructions across different benchmarks including VIMABench and the CaP benchmark.

### Strengths
1. This system conducts experiments on diverse benchmarks such as VIMABench and the CaP benchmark.

2. Detailed ablation studies are also provided, highlighting the efficacy of 'Library API Full Examples' and different segmentation methodologies.

### Weaknesses
1. Important related work RT-2 [1] is missing, likely because it is too recent to be included and discussed.

2. The improvement in performance is not robust. Figure 5 showcases results from evaluations on VIMABench. However, the baseline VIMA-200 performs slightly better than the suggested approach across all tasks. Although the authors argue that VIMA requires large-scale pre-training, their proposed method also depends on large-scale pre-trained foundation models, such as SAM. It would be beneficial for the authors to demonstrate performance gains on tasks where VIMA has not been trained. Furthermore, the performance gain of 3% over PerAct and 1% over CaP in Table 1, is also not significant. The performance gains are also not presented with statistical significance, which makes it hard to assess if the gains are meaningful.

3. Although employing cursor clicks to create point prompts and guide SAM’s segmentation is clever, applying this approach for the Pick and Place task seems unnecessary. If you have the camera extrinsics, you can easily obtain the 3D location of the click by projecting from the image space to the 3D space, given the depth or known height. In this case, there's no need for SAM. In fact, other example tasks should be selected to better highlight the advantages of the proposed method.

### Questions
This work mentions the utilization of two types of LLMs: text-davinci-003 and LLaMA-Adapter. Could you provide an explanation on the performance differences between these two?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
