# Benchmarking Visual Cognition of Multimodal LLMs via Matrix Reasoning

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Recently, Multimodal Large Language Models (MLLMs) and Vision Language Models (VLMs) have shown great promise in language-guided perceptual tasks such as recognition, segmentation, and object detection. However, their effectiveness in addressing visual cognition problems that require high-level multi-image reasoning and visual working memory is not well-established. One such challenge is matrix reasoning -- the cognitive ability to discern relationships among patterns in a set of images and extrapolate to predict subsequent patterns. This skill is crucial during the early neurodevelopmental stages of children. Inspired by the matrix reasoning tasks in Raven’s Progressive Matrices (RPM) and Wechsler Intelligence Scale for Children (WISC), we propose a new dataset MaRs-VQA and a new benchmark VCog-Bench to evaluate the zero-shot visual cognition capability of MLLMs and compare their performance with existing human visual cognition investigation. Our comparative experiments with different open-source and closed-source MLLMs on the VCog-Bench revealed a gap between MLLMs and human intelligence, highlighting the visual cognitive limitations of current MLLMs. We believe that the public release of VCog-Bench, consisting of MaRs-VQA, and the inference pipeline will drive progress toward the next generation of MLLMs with human-like visual cognition abilities.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the high-level visual cognition abilities that require multi-image reasoning, by investigating matrix reasoning. A new benchmark is proposed:  MARS-VQA which contains 1440 instances and VCogBench to evaluate matrix reasoning abilities.  The paper finds that similar to previous findings with RAVEN's matrices and other similar tests, state of the art MLLMs struggle at matrix reasoning and perform worse or slightly better than random (25%) performance on a four-way classification task.

### Strengths
1. Paper is well structured and experiments are comprehensive in terms of the number of models evaluated.
2. MLLM evaluation is an important challenge and the paper seeks to address that question with a connection to human psychometric evaluation.

### Weaknesses
1. The claim that matrix reasoning has been "proven to be used to test human intelligence" or that "matrix reasoning is an important reflection of many fundamental capabilities of human intelligence" are to say the least, as controversial as saying "IQ Tests" are a true reflection of human intelligence.
2. The benchmark is restricted to shapes but could have potentially also used natural images. In my opinion, making claims about human visual cognition where the test data is purely symbolic is an overclaim. It could be an evaluation of human symbolic cognition.
3. The experiments include prompts designed for this task -- the influence of this choice of prompts on the performance is unclear.

### Questions
1. What are the insights from the paper? Why are we interested in testing matrix reasoning of VLMs and why do we want VLMs to succeed at this task? Besides observing that VLMs aren't good at this task, what should VLM researchers and developers should take away from this work?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a new dataset MaRs-VQA and a new benchmark VCog-Bench to evaluate the zero-shot visual cognition capability of MLLMs with a matrix reasoning task. It requires MLLMs to discern relationships among patterns in a set of images and extrapolate to predict subsequent patterns. This paper proposes two evaluation pipelines of the proposed VCog-Bench: (1) Multi-image reasoning via CoT and (2) direct image input and text output. The evaluations are performed on various MLLMs of both APIs and open-source models.

### Strengths
1. The paper is clear and easy to follow.

2. The evaluations are performed on various MLLMs of both APIs and open-source models.

3. It reveals the current MLLMs still need to improve on matrix reasoning.

### Weaknesses
1. The contribution of this paper is incremental. 
- The proposed MaRs-VQA and VCog-Bench are all sourced from existing well-built datasets, including MaRs-IB, RAVEN, and CVR.
The proposed multi-image reasoning via CoT method is an application of CoT to a particular task. It is not a general solution for other tasks. 
- The conclusion of the limitation of current MLLMs is not supported by sufficient evidence and is not convincing. How the author attains the conclusion that current MLLMs have Limited Use of Visual Information and Restricted Visual Working Memory needs to be clarified. 
2. The experiments show that the MLLMs perform much worse than humans. It is unknown if it is because the MLLMs do not understand the task to perform. The author may evaluate MLLMs with in-context learning, which can take one or two QA paris as examples. 
3. Additionally, it will be interesting to discuss if the MLLMs can easily attain the ability to solve matrix reasoning via training in a small number of cases. For example, the model can be trained on a small subset of MaRs-VQA and evaluated on VCog-Bench.

### Questions
Due to the incremental contributions of this paper, I tend to be borderline negative in the current stage. Please refer to the weakness section for detailed comments.



###################

Thank you for your explanation; it addresses part of my concerns. However, I still feel that the contribution of this work falls below the standard expected for ICLR. Firstly, MaRs-VQA and VCog-Bench are derived from the questionnaires of MaRs-IB, RAVEN, and CVR. While these datasets structure the task as VQA, I believe the questionnaire images themselves inherently serve as both questions and answers. As such, MaRs-VQA and VCog-Bench merely reformulate them, which represents a relatively minor contribution compared to the original questionnaires. Secondly, the discussion on the limitations of current MLLMs emphasizes their difficulties in handling multiple sub-tasks simultaneously. However, it is just a conjecture, as the evidence provided in the paper is insufficient to substantiate this claim.

Overall, I will keep my rating.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces MaRs-VQA as a new matrix reasoning VQA dataset, and VCog-Bench as a visual cognition benchmark to evaluate the matrix reasoning performance of 16 existing MLLMs in the zero-shot setting. The thorough experiments qualitatively reveal the visual cognition gap between MLLMs and humans in matrix reasoning problems.

### Strengths
1. The proposed MaRs-VQA dataset and VCog-Bench benchmark help establish the cognitative training and evaluation pipeline for multi-modal large language model.

2. The evaluations experiments are comprehensive and include extenstive MLLMs.

3. Some of the insights found in experiments can inspire more future investigations.

### Weaknesses
1. The motivation is unclear. It is not clear how the proposed MaRs-VQA differs from the privious ones. From Table 1, it seems the most remarkable difference is the introduction of RGB image.

2. The authors claim that "This setting makes current matrix reasoning assessment an ill-posed problem because such tests accurately reflect reasoning capability only when subjects engage without prior training, i.e., in zero-shot inference settings." It is quite confusing since the training-testing paradigm is the common methodology. As long as the training and test sets do not overlap, why does this pattern not make sense?

3. In multi-image reasoning evaluation of Table 2, only GPT and Claude evaluated. Why the open-source models not included?

4. In Table 4, the authors claim that "The difficulty level is based on the complexity of color, size, geometry, positional relationships, and object counting." However, it is not clear how the difficulty level is related to the mentioned elements. More details should be presented.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new dataset called MaRs-VQA and a benchmark named VCog-Bench to evaluate how well MLLMs understand and reason about visual information. It focuses on testing these models using matrix reasoning tasks, which are inspired by established intelligence tests like RPM and the WISC. These tasks require advanced visual reasoning, which is still challenging for current AI models. The paper compares how different MLLMs perform in these tasks compared to humans, showing a clear gap in capabilities. The contributions include making MaRs-VQA, the largest dataset designed by psychologists for matrix reasoning, and introducing VCog-Bench as a new standard for evaluating visual cognition. The experiments show the current limitations of MLLMs in dealing with abstract visual problems and provide suggestions for future improvements.

### Strengths
- The paper focuses on a challenging area of visual cognition relevant for assessing human-like intelligence. Unlike many studies that emphasize perception-based tasks (e.g., object detection), this work addresses higher-level reasoning and working memory. The MaRs-VQA dataset, based on established psychological tests, offers a diverse and validated dataset for visual cognition.
- The work highlights a gap between human and machine cognition in abstract visual reasoning, even for advanced models like GPT-4o. By focusing on more sophisticated visual cognition, the paper encourages the development of models that can reason about images abstractly, not just recognize them. This has important implications for the progress of AGI.
- The paper is well-structured, with clear definitions of each dataset, model, and experimental setup. The comparison between human and model performance is effective in showcasing current limitations and areas for improvement.

### Weaknesses
 - The paper does not explore how changes in the visual complexity of MaRs-VQA impact model performance. It is unclear whether models are sensitive to subtle changes (e.g., color gradient variations or object overlaps), which could provide important insights into model robustness and areas for improvement.
- One of the weaknesses is the lack of detailed analysis into why specific models fail at particular reasoning tasks. However, considering that the primary goal of the paper is to propose a new dataset, this focus on benchmarking rather than in-depth analysis of is understandable.

### Questions
- Could the authors explore how changes in the visual complexity of MaRs-VQA impact model performance? Are models sensitive to subtle changes, such as color gradient variations or object overlaps?
- The paper showed zero-shot performance as an evaluation criterion. Could few-shot learning approaches be explored as a transitional step to understand whether MLLMs can improve their performance incrementally?
- How might MLLMs be modified to better retain visual information during the reasoning process? Want to hear the authors' opinion.

### Soundness
2

### Presentation
3

### Contribution
3
