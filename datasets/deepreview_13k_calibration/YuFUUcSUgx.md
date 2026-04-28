# You Can Train from Scratch: Further Discussion on the Long Range Arena

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 1, 5

## Abstract
Despite their success, Transformers suffer from quadratic complexity in the sequence length, limiting their applicability to long-range dependency problems and making them expensive to train and run. After many proposals to address this issue, the Long Range Arena (LRA) was suggested as a benchmark to evaluate the performance of new models in long-range dependency modeling tasks. The Transformer and its variants performed poorly on this benchmark, and a new series of architectures such as State Space Models (SSMs) gained some traction, greatly outperforming Transformers in the LRA. Recent work has shown that with a denoising pretraining phase, Transformers can achieve competitive results in the LRA with these new architectures. In this work, we discuss and explain the superiority of architectures such as MEGA and SSMs in the Long Range Arena, as well as the recent improvement in the results of Transformers, pointing to the positional and local nature of the tasks. We show that while the LRA is a benchmark for long-range dependency modeling, in reality most of the performance comes from short-range dependencies. By using rotary embeddings and training techniques to mitigate its data inefficiency, the Transformer is also able to reach state-of-the-art performance without a separate pretraining phase. What is more, with the same techniques, we are able to remove all restrictions from SSM convolutional kernels and learn fully parameterized convolutions without decreasing performance, suggesting that the design choices behind SSMs merely added inductive biases and learning efficiency for these particular tasks. Our insights indicate that LRA results should be interpreted with caution and call for a redesign of the benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work focuses on the performance of Transformer architecture on the Long Range Arena benchmark (LRA). Earlier works have shown that simple state-space / recurrent architectures can achieve better performance than Transformer architectures on LRA benchmark, while transformers are still the preferred choice in real-world sequential dependency modelling. Although Transformers can achieve on-par performance on LRA using a pre-training phase with a denoising objective, this leads to additional computational cost and risk of representation collapse. This works shows that Transformers can achieve similar performance on LRA benchmark without an additional pretraining stage with the help of better data augmentation strategies and rotary positional embeddings. This work argues that the tasks in LRA have a positional bias and LRA benchmark should be interpreted with caution.

### Strengths
- Incorporating data augmentation during transformer training helps avoid the pre-training stage and still achieves comparable results as state-of-the-art models for LRA benchmark.
- Ablations on positional embeddings show that transformers improve in performance with better positional embeddings. 
- This work points out flaws in the popular LRA benchmark and urges to use this benchmark with caution.

### Weaknesses
 - LRA has been known to have local positional bias in the literature (see R1, R2). R2 already incorporates some form of positional embeddings in the transformer architecture helps achieve better performance on LRA benchmark.
- Data augmentation would help improve performance of any model on this benchmark
- Proposed techniques in this work are marginal since pre-training in R2 already shows the objective which is used in this paper along with positional embeddings. Similarly, data augmentation techniques are well known in the literature to improve model performance.

### Questions
- This work mentions the risk of representation collapse in the two stage training, do you have any concrete evidence that such a collapse happens in your experiments?
- Do you know why gMLP does not improve on text-retrieval task with your setup in Sec. 4.2?
- Does the same conclusion hold true for other long range dependency benchmarks such as SCROLLS?
- Can you provide an estimate of resources required for training on Pathfinder vs Path-X tasks?
- Can you compare the performance of MEGA, S4, S5 when these models are trained with data augmentation strategies mentioned in this work?
- In Figure 2, why is only gMLP trained with the proposed data augmentation strategies? Why weren't these techniques applied on S4/S5?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper revisits prior results on the LRA benchmark and shows that rather than a separate pretraining phase, alternative training techniques can be applied to each task to achieve similar results with Transformers. Furthermore, the same training approach allows fully parameterized convolutions to match the performance of parameterized convolutions, such as SSMs. The authors provide a discussion on the importance of positional and locality bias in LRA tasks, showing that strong performance can be achieved with either a correct choice of positional embeddings or strong locality bias, despite the long range nature of the tasks.

### Strengths
* Benchmarks such as LRA are in widespread use for developing new architectures, questioning what are the key elements required to reach competitive results on them is an important question.

* The suggested approaches, of applying a different training strategy to each task, leads to competitive results - I especially like the approach in pathfinder, adding easier samples to induce a stronger signal early in training.

* The discussion in section 4.3 is insightful:

   * The importance of the correct choice of positional information is clearly explained.

   * The results for a convolution model in Table 2 are surprising and insightful, indicating importance of locality in the tasks.

### Weaknesses
 * The broader implications of the main result, sections 4.1, 4.2 are unclear. If the claim is that LRA tasks are unrepresentative for performance on real world tasks it is unclear how results in 4.1,4.2 imply that. Alternatively, if the authors claim that their training setup is more realistic then prior work, it should be clearly stated and argued for with empirical results. If there are any additional implications I could not understand them from the text.

* Benchmarks such as LRA are designed to evaluate architecture inductive bias, introducing additional biases via other training strategies, such as augmentations, couples the modeling and augmentation induced biases.

   * For CIFAR10 the augmentations are not clearly described, looking in cited work [1] it seems that the augmentations are:  “...A sub-policy consists of two operations, each operation being an image processing function such as translation, rotation, or shearing, and the probabilities and magnitudes with which the functions are applied.” These augmentations are based on the 2D structure of the input and provide additional signal for the model to recognize it - which is part of the purpose of this task [2].

   * SImilarly for ListOps, it is desirable from a sequence model to learn the permutation invariant nature of the task from the data.

* It is not clear if the same training approach applied to Transformers and gMLP is used on the baselines (MEGA, S4 etc.). Results seem to be the same as those in cited work but this is not clearly stated - whether the performance gap still persists when models are trained in the same manner is important to the claim that Transformers can match performance.

### Questions
* In the introduction, the important question about: “how representative the LRA benchmark results are of long-range dependency modeling performance” (4th paragraph) is raised but I could not understand if it is explored later in the text - if it is not addressed, results connecting or disconnecting performance on LRA and real-world tasks can benefit the paper.

* Throughout the text it is mentioned that avoiding the pretraining phase reduces the risk of representation collapse - why does representation collapse matters when training on a single downstream task and reaching competitive results?

* In section 2.5 equation 5 the what is the definition of the `split` operation

* In table 2, Can you clarify the calculation of the receptive field? How does a kernel with size 61 have a receptive field of 30 tokens?

[1]  Ekin D. Cubuk, et. al.  Autoaugment: Learning augmentation strategies from data

[2] Yi Tay et. al LONG RANGE ARENA: A BENCHMARK FOR EFFICIENT TRANSFORMERS

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper explores the performance of Transformer models on the Long Range Arena (LRA) benchmark, which evaluates models' ability to handle long-range dependencies across diverse tasks in text, image, and mathematical domains. Traditionally, Transformers face challenges with quadratic complexity relative to sequence length, limiting their scalability and efficiency. While newer architectures like State Space Models (SSMs) have outperformed Transformers on the LRA, recent work by Amos et al. demonstrated that Transformers could achieve competitive results through a denoising pretraining phase. Building on this, the authors of this paper present training techniques that enable Transformers to attain similar or superior performance on the LRA without requiring a separate pretraining stage. These techniques include task-specific data augmentation, integrating a denoising objective within a multi-task learning framework for text tasks, and employing rotary embeddings for positional encoding. Through ablation studies, the paper reveals that many LRA tasks are predominantly positional and heavily reliant on short-range dependencies. This insight suggests that inductive biases favoring locality significantly enhance model performance. Additionally, the paper evaluates the gMLP architecture, demonstrating that unrestricted long-convolution-based models can surpass specialized architectures like SSMs on most LRA tasks. The authors conclude by cautioning that LRA benchmark results should be interpreted with an understanding of the models' inductive biases and the specific nature of the tasks, as these factors heavily influence performance outcomes.

### Strengths
The paper comprehensively analyzes the factors contributing to the Transformer's performance on the Long Range Arena benchmark. Exploring training techniques that eliminate the need for a separate pretraining phase addresses computational efficiency and simplifies the training pipeline.

### Weaknesses
 * Novelty and originality: The paper does not introduce a new model. It leverages existing techniques, such as Rotary embeddings and data augmentation, making it purely applied / engineering work. The authors should clarify what they consider their work's main novelty or contribution beyond applying these existing methods.
* Depth of Analysis: The discussion provides valuable insights into the role of inductive biases and the characteristics of LRA tasks. However, it would benefit from a deeper exploration of these findings. Specifically, the authors should provide more detailed explanations of why certain training techniques are effective and theoretically explain how rotary embeddings improve performance. This additional analysis would strengthen the paper's contribution by offering a deeper understanding of the underlying factors influencing model performance.
* Poor experimental results: The evaluation is limited to the LRA dataset, which does not comprehensively demonstrate the models' capabilities on longer sequences. To improve the robustness of the findings, the authors should consider including additional benchmarks such as RULER (https://github.com/hsiehjackson/RULER) and the Path-X dataset from LRA. Additionally, updating their comparisons to include the most recent state-of-the-art results, not only MEGA, would provide a more current and thorough evaluation of their methods. Addressing these points would significantly improve the comprehensiveness and relevance of their experimental results.
* Already studied a lot: LRA has been studied a lot at this point and is not so important for long sequence modeling. SSMs solved it.

### Questions
No further questions.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors analyze the Long-Range Arena dataset regarding the locality of relevant features for the prediciton tasks. They find that using very localized features in a convolution based architecture can give performances very close to SOTA, rendering Long-Range Arena effectively a "non-long-range" benchmark. They show how augmentation techniques can help achieving SOTA-like performance with Transformers using rotational positional embeddings - a technique well-known from other modalities (vision) for compensating the lack of inductive bias in Transformer models.

### Strengths
They can show that Long Range Arena can be "solved" to SOTA levels using very short convolution windows, rendering it a non-long range benchmark effectively.

### Weaknesses
The authors may analyze the Long-Range Arena dataset further in how it is actually not a long-range dataset. 
The augmentation techniques used for reaching good performance on LRA with Transformers are well-known and are expected to benefit training.
For a clear accept / strong accept, I would expect a construction / assembly of a benchmark that actually tests long-range reasoning (beyond simple retrieval as in MQAR / AR / Needle in the Haystack tasks). The analysis of the LRA dataset could be more rigorous, for example by quantifying the effective receptive field required for each task, and showing the distribution of distances between relevant tokens. The current analysis focuses on the performance of small convolution windows, but a more detailed analysis of the data itself would be beneficial. Furthermore, the paper could benefit from a more thorough discussion of the limitations of the augmentation techniques used, and in which scenarios they might not be sufficient to achieve good performance.

### Questions
Do you have ideas on how to improve upon the LRA dataset as a benchmark for long-range modeling?
Are there ideas for long-range tasks where (simple) augmentation techniques might fail?
The presentation of well-known Transformer and SSM architectures is unnecessary in that detail in my opinion.

### Soundness
3

### Presentation
3

### Contribution
2
