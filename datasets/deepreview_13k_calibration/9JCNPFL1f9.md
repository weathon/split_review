# Visual Haystacks: A Vision-Centric Needle-In-A-Haystack Benchmark

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
Large Multimodal Models (LMMs) have made significant strides in visual question-answering for single images. Recent advancements like long-context LMMs have allowed them to ingest larger, or even multiple, images. However, the ability to process a large number of visual tokens does not guarantee effective \textit{retrieval} and \textit{reasoning} for multi-image question answering (MIQA), especially in real-world applications like photo album searches or satellite imagery analysis. In this work, we first assess the limitations of current benchmarks for long-context LMMs. We address these limitations by introducing a new vision-centric, long-context benchmark, ``Visual Haystacks (VHs)''. We comprehensively evaluate both open-source and proprietary models on VHs, and demonstrate that these models struggle when reasoning across potentially unrelated images, perform poorly on cross-image reasoning, as well as exhibit biases based on the placement of key information within the context window. Towards a solution, we introduce MIRAGE (Multi-Image Retrieval Augmented Generation), an open-source, lightweight visual-RAG framework that processes up to 10k images on a single 40G A100 GPU---far surpassing the 1k-image limit of contemporary models. MIRAGE demonstrates up to 13\% performance improvement over existing open-source LMMs on VHs, sets a new state-of-the-art on the RetVQA multi-image QA benchmark, and achieves competitive performance on single-image QA with state-of-the-art LMMs. Our dataset, model, and code are available at: \href{https://visual-haystacks.io}{https://visual-haystacks.io}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors presents Visual Haystacks (VHs), a new vision centric benchmark designed to assess the performance of Large Multimodal Models (LMMs) in the multi-image question answering (QA) task. In addition, the author proposes a new visaul-RAG framework, MIRAGE, to enhance the task performance.

### Strengths
* Novel Multi-Image QA Benchmark: The authors introduce an interesting multi-image QA benchmark, Visual Haystacks, designed around a vision-centric "needle-in-a-haystack" scenario, providing a fresh and challenging setting for the LMM evaluation.

* Comprehensive Model Evaluation:  The paper conducts a thorough evaluation of LMMs on the VHs benchmark, uncovering important insights into current models, such as vulnerability to visual distractors, challenges with multi-image understanding, and tendencies toward positional visual bias.

* Novel Visual RAG Framework: The authors introduce a novel visual RAG framework that combines a compressor and a retriever. The compressor efficiently processes up to 10,000 images on a single 40GB A100 GPU, while the retriever identifies the top-k most relevant images for a given question, enhancing the framework’s scalability and efficiency.

### Weaknesses
 * Limited Object Diversity: The authors constructed the VHs benchmark using objects from the COCO dataset, which contains only 80 object categories. This limited selection may restrict the diversity and comprehensiveness of the benchmark, potentially affecting its ability to evaluate models across a broader range of visual scenarios. The lack of fine-grained categories within COCO, such as different types of vehicles or animals, further limits the benchmark's ability to assess nuanced visual understanding. For example, distinguishing between a sedan and a truck, or a husky and a golden retriever, is not possible within the current object set, which restricts the benchmark's capacity to evaluate detailed visual reasoning.

* Restricted Question Diversity: The authors appear to rely on a few simple templates to generate questions, which may restrict the variety of question types in the benchmark. This reliance on templates could lead to models exploiting superficial patterns in the questions rather than demonstrating genuine visual understanding. For instance, if all questions follow a similar structure, models might learn to associate specific keywords with particular answers without actually processing the visual content deeply. The lack of questions that require comparative reasoning or attribute-based queries further limits the benchmark's scope.

* More like Object Detection than QA Reasoning: Many questions in the benchmark (e.g., "For the image with a truck, is there a dog?") seem to primarily assess the model’s object detection abilities rather than its visual QA reasoning skills. It is questionable if the benchmark requires the advanced visual QA reasoning skills from the models. The questions often involve simple presence/absence checks of objects, which can be solved by basic object detection algorithms. The benchmark does not adequately test the models' ability to perform more complex reasoning tasks, such as understanding spatial relationships, object interactions, or contextual cues.

* Missing Related Work: The paper does not reference several recent multi-image QA benchmarks, for example:
 1. CompBench: A Comparative Reasoning Benchmark for Multimodal LLMs
 2. MANTIS: Interleaved Multi-Image Instruction Tuning
 3. MUIRBENCH: A Comprehensive Benchmark for Robust Multi-Image Understanding.

Additionally, a similar multi-image retrieval approach was introduced in "ColPali: Efficient Document Retrieval with Vision Language Models", but this work was also not cited.

### Questions
Please see the weakeness. In addition,
* How many templates were used to generate questions?
* What advantages does the VHs benchmark offer compared to recent multi-image QA benchmarks?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses the limitations of Large Multimodal Models (LMMs) in multi-image question answering, where handling large visual contexts does not ensure effective retrieval and reasoning across images. Current benchmarks reveal biases and challenges in MIQA, such as poor cross-image reasoning and sensitivity to information placement. To overcome these, the authors propose "Visual Haystacks (VHs)," a vision-centric benchmark that tests retrieval and reasoning over multiple images, highlighting models' struggles with visual distractors and multi-image reasoning. They also introduce MIRAGE, an open-source Multi-Image Retrieval Augmented Generation framework capable of handling up to 10,000 images on a single GPU, achieving significant improvements over existing models and setting new standards in MIQA benchmarks like RetVQA. Key contributions include VHs, systematic LMM evaluation, and MIRAGE's scalable MIQA capabilities.

### Strengths
- I generally feel the direction is important to our community where design meaningful Visual Haystack benchmark for evaluating VLM. 
- Some interesting points are discovered when evaluating models on the proposed benchmark. Since random guess could achieve 50% accuracy in the proposed benchmark, some open-sourced VLMs performance significantly drop even the Haystack size is very small. However, those models maintain high scores in some public evaluation-datasets. 
- Some detailed experiments are conducted such as needle position and running time. 
- The proposed benchmark are made publicly available under MIT license, which is good for community.

### Weaknesses
 - Benchmark construction is still mainly centered around recognition tasks, based on benchmark design principles listed in Line129~138. Basically, it requires a strong recognition among all the input images, rather than true visual reasoning. The Visual Haystacks (VHs) benchmark, while useful for evaluating retrieval, primarily assesses the ability to locate specific objects across multiple images, which is fundamentally a recognition task. This limits its capacity to evaluate more complex visual reasoning abilities, such as understanding spatial relationships, inferring object interactions, or performing abstract scene understanding.
- Based on the Figure 2 and 3, certain models, such as Gemini, GPT and the proposed MIRAGE, consistently perform better on the proposed multi-needle challenges compared to single-needle tasks. However, the multi-needle challenges are intentionally designed to be more difficult, as they demand additional reasoning across multiple images. This raises concerns about the benchmark's design, as it appears that the increased complexity of multi-needle tasks does not translate to a corresponding decrease in model performance, potentially indicating a flaw in how the difficulty is calibrated or a bias in the evaluation.
- Since the benchmark is constructed in way of examining recognition, therefore the proposed method contain ad-hoc modules, such as "a retriever module then calculates relevance scores, ensuring that only the most relevant images are passed to the LLM for final reasoning." This design choice appears to be tailored specifically to the recognition-focused nature of the benchmark. The retriever module, while potentially beneficial for handling large image sets, might not be necessary or even beneficial for general visual reasoning tasks. For example, many of the tested single image dataset used in this paper, do not need this retriever module at all. The inclusion of this module raises questions about the generalizability of the proposed method to tasks that require more holistic visual understanding.
- The proposed framework achieved not-very-good performance on some of the tested datasets. Also, there are many datasets that not being tested such as SEED, MME, and CHAIR.

### Questions
- Could you please address the points raised in the above weakness?
- Could you please add some randomly sampled failure cases made by GPT or Gemini? Sometimes failure cases can tell more than good cases. 
- Could you please address the ethics concerns around the code license?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a long context, visual needle in a haystack benchmark which composed of 1k yes/no questions changeling the model to reasoning and find the target object in the images. It evaluated on both open-source and closed-source LMMs and reveal several critical findings such as susceptibility to visual distractors, difficulty in multi-image reasoning, and a bias in image positioning. It introduces a new baseline called MIRAGE (Multi-Image Retrieval Augmented Generation) for better handling of VH tasks.

### Strengths
1. This paper introduced a new visual needle in a haystack benchmark which composed of 1k yes/no questions. 
2. Evaluated on both open-source and close-source models and gained three insightful findings. 
3. Introduced a new baseline called MIRAGE for better handling of visual haystack tasks.

### Weaknesses
1. The questions are only limited to yes/no questions. 
2. The question template are very limited, seems only three. 
3. MIRAGE has a significant performance drop in 4 out of 7 general VQA tasks. 
4. The approach of MIRAGE, deselecting unrelated (distracting) images somehow circumvents the VH challenge, as the this challenge lies in how model can reasoning in long context.  
5. The task of finding a target object seems still not simulating a real world scenario of long context visual reasoning task.

### Questions
1. I'm confused about the difference between the MIRAGE model in Table 1 and the Q-former Model in Table. Doesn't MIRAGE utilize Q-former. 
2. See above.

### Soundness
3

### Presentation
2

### Contribution
2
