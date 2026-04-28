# DNALONGBENCH: A Benchmark Suite For Long-Range DNA Prediction Tasks

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6

## Abstract
Modeling long-range DNA dependencies is crucial for understanding genome structure and function across a wide range of biological contexts in health and disease. However, effectively capturing the extensive long-range dependencies between DNA sequences, spanning millions of base pairs as seen in tasks such as three-dimensional (3D) chromatin folding, remains a significant challenge. Additionally, a comprehensive benchmark suite for evaluating tasks reliant on long-range dependencies is notably absent. To address this gap, we introduce DNALONGBENCH, a benchmark dataset spanning five important genomics tasks that consider long-range dependencies up to 1 million base pairs: enhancer-target gene interaction, expression quantitative trait loci, 3D genome organization, regulatory sequence activity, and transcription initiation signal. To comprehensively assess DNALONGBENCH, we evaluate the performance of five baseline methods: a task-specific expert model, a convolutional neural network (CNN)-based model, and three fine-tuned DNA foundation models -- HyenaDNA, Caduceus-Ph and Caduceus-PS. We envision DNALONGBENCH having the potential to become a standardized resource that facilitates comprehensive comparisons and rigorous evaluations of emerging DNA sequence-based deep learning models that consider long-range dependencies.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a set of five benchmarking tasks for genomic language models, with a focus on tasks that involve modeling long-range DNA dependencies, including enhance-target gene interaction and 3D genome organization. These tasks represent a diverse set of biologically important characteristics. The authors benchmark five baseline methods on each task - task-specific expert models, CNN-based models, and three recent DNA language models, and find that the DNA language models they benchmark do not outperform the task-specific models.

### Strengths
- The tasks included in the benchmark are biologically significant and diverse, especially the focus on tasks with different dimensionalities (1D or 2D) and granularities (binned or base pair level). In addition, the paper does a good job explaining the biological significance of each task. Both the increased focus on long-range tasks and base pair resolution tasks represent novel aspects of this benchmark compared to other previously published benchmarks.
- The results are presented in a clear and concise manner
- The performance of the three evaluated DNA language models — HyenaDNA, Caduceus-Ph, and Caduceus-PS — on these tasks reveal important limitations of current DNA language models at modeling long range dependencies, even when the models are able to incorporate long context lengths.

### Weaknesses
 - In my opinion, the main weakness of this paper is novelty. Although the benchmarking tasks are important and biologically motivated, all five of the tasks and corresponding datasets have already been used to benchmark models in previous publications and in some previous benchmarks, such as BEND (Marin, et al. 2023) and LRB (Kao, et al. 2024). The “Regulatory sequence activity” task directly uses the training, validation, and test set sequences from Enformer. Therefore, the main contribution of this paper is consolidating these tasks into one resource and comparing the performance of DNA language models and more traditional supervised approaches. One potential way to increase the novelty and contribution of this work could be to incorporate more datasets that weren’t used in previous publications to increase the amount of benchmarking data for each task. For example, for the enhancer-target gene task, the dataset is relatively small, and different experimental datasets often suffer from their own technical and experimental biases. Since a number of similar datasets exist and are publicly available, it would improve and increase the impactfulness of the benchmark to aggregate multiple similar datasets.

 - The term “Expert model” is misleading. For example, L369-370 refers to “expert models tailored to each task,” but in some cases, such as using Enformer as an expert model for eQTL prediction, the expert model has not actually been tailored to this task. An alternative could be to refer to these models at “State of the art models.” In addition, in some cases the choice of Expert/SOTA model could be revisited. For example, for the enhancer-target gene task, Enformer (Avsec et al. Nature Methods (2021)) or Borzoi (Linder et al. 2023) should be used as a state of the art model instead of Activity by Contact.  In addition, for the eQTL prediction task, Borzoi was shown to outperform Enformer in Linder et al. 2023.
- Use of the term DNA foundation model and which models are classified in this category is inconsistent throughout the paper. For example, on L146, Avsec et al. 2021a is cited as a DNA foundation model (although it is not actually pre-trained on only DNA seqeunces), but later in the paper it’s used as an “expert model” baseline in contrast to the DNA foundation models.


### Questions
- The term “Expert model” is misleading. For example, L369-370 refers to “expert models tailored to each task,” but in some cases, such as using Enformer as an expert model for eQTL prediction, the expert model has not actually been tailored to this task. An alternative could be to refer to these models at “State of the art models.” In addition, in some cases the choice of Expert/SOTA model could be revisited. For example, for the enhancer-target gene task, Enformer (Avsec et al. Nature Methods (2021)) or Borzoi (Linder et al. 2023) should be used as a state of the art model instead of Activity by Contact.  In addition, for the eQTL prediction task, Borzoi was shown to outperform Enformer in Linder et al. 2023.
- Use of the term DNA foundation model and which models are classified in this category is inconsistent throughout the paper. For example, on L146, Avsec et al. 2021a is cited as a DNA foundation model (although it is not actually pre-trained on only DNA seqeunces), but later in the paper it’s used as an “expert model” baseline in contrast to the DNA foundation models.

Minor suggestions:
- L51-53 - Karollus et al. Genome Biology (2023) could be cited with reference to this point
- L154-155 is unclear and should be reworded: “It has shown promising performance in long-range species classification tasks despite the problem itself is not well defined in real applications.”

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents DNALongBench, which consists of 5 datasets which attempt to test a predictive model’s ability to make predictions on DNA sequences which are somewhat related to long-range interactions in the genome. Each of these datasets consists of a set of inputs and outputs, along with a well-defined performance metric. The input is a long DNA sequence and the output is a label which can be a scalar, or one or more functional-readout profiles which are parallel to the input sequence.

These 5 datasets and tasks are: 1) given a sequence with an enhancer and a promoter in it, predict whether or not the enhancer is linked to the promoter functionally; 2) given a long sequence, predict the (symmetric) 2D contact map; 3) given a DNA sequence, predict the functional profiles of several regulatory-genomic assays in both human and mouse; 4) given the reference and mutated sequences of putative eQTLs, predict whether or not the eQTL is causal/functional; 5) given a DNA sequence, predict base-pair-level profiles of transcription initiation.

For each task, the authors computed the performance of the dataset on HyenaDNA and Caduceus, which have been fine-tuned for each task separately. They also trained a simple CNN as a baseline, and compared to an “expert model”, which is the model which was trained specifically for that task. The authors report the resulting performance metrics, and describe some general trends, such as the observation that the expert model generally performed the best, and that the long-range language models (e.g. HyenaDNA) typically underperformed.

### Strengths
### Good test of actual functional abilities of long-range DNA language models

In the recent literature, a lot of effort has been made to port over LLMs from NLP to DNA sequences (and other biological tasks). In these works, the evaluation of DNA LLMs has been very sparse, and it was unclear as to whether or not these models could handle real biological tasks of significance (instead of very simplistic predictive tasks like species prediction, which is not biologically meaningful or challenging today as a computational task).

This paper offers a much-needed evaluation of whether or not these DNA LLMs can actually handle biologically meaningful and challenging tasks which rely on long-range interactions (which was the initial promise of these models). Through various experiments, this paper shows that, in fact, these DNA LLMs are not particularly well-poised to predict meaningful biological tasks, even after fine-tuning.

### Good selection of benchmarks with meaningful biological significance

The selection of the 5 benchmark tasks is well-thought-out, and they span many areas of interest, from regulatory genomics, to chromatin organization, to variant-effect prediction (for eQTLs). Together, these tasks cover a decent space in testing the ability of models to capture trans effects in the genome.

### Clear writing and well-organized paper

The paper is well-written, with clear organization and motivation. Reading through, things were simple to understand, and structured in a very good way.

### Weaknesses
### Other than large DNA language models, not many other models are tested

The DNA LLMs that were tested (i.e. HyenaDNA and Caduceus) are good representations of this sort of model, but there aren’t that many other models that were tested in this benchmark. Other than these DNA LLMs, this work trains a very simplistic CNN, and applies a single expert model (generally, the model which was published along with the data). Together, the expert model is an example of one of the best models possible, and the CNN is an example of one of the easiest deep-learning-based baselines. The analyses in this paper show how DNA LLMs perform relative to these two endpoints, but there are not any other models that are tested.

In addition to these DNA LLMs, many researchers will use other models and architectures which can also detect long-range interactions (such as those described in section 2.2). Especially due to the computational cost of DNA LLMs, many researchers will necessarily be relying on other architectures. It would be much more informative to show the performance of these other architectures (e.g. Enformer, Borzoi, even DanQ, etc., both fine-tuned and not fine-tuned on the specific task), to see how these models also perform. In its current form, this paper is largely just a benchmark for DNA LLMs, even though several other models exist, whose performance also falls somewhere in the spectrum between the basic CNN and the expert model. It would be far more meaningful of a benchmark if those models are shown, as well.

### Limited results on the various advantages and disadvantages of certain models

There are only limited results in the paper exploring and discussing the relative advantages and disadvantages of certain models. For a benchmarking paper, it would be useful to have more discussion on the various areas where certain models do better than others, and an exploration of why (including different ablation studies). Some interesting discussion points (a very non-comprehensive set of suggestions) may be:

- How useful is reverse-complement augmentation or reverse-complement-aware architectures for these tasks?
- Since the expert model really does much better, how much of its improved performance is due to its focus on a specific task (whereas the DNA LLMs are not trained on a specific task)? How much does fine-tuning the DNA LLMs allow them to perform much better on these specific tasks?
- How much performance is gained from the sheer size/expressivity of the DNA LLMs? Would a different architecture of similar size/expressivity be comparable to the DNA LLMs (e.g. testing an Enformer-like architecture of high capacity, for each of these tasks).
- Section 5.2 suggests a difference between long-range and short-range prediction performance in these models. Is the failure of DNA LLMs to predict specific peaks due to the excessively long input sequences (i.e. so the model has a hard time focusing on specific parts of a sequence)?

### Suggestions for improvements in writing

There are several places where the paper has some typos or other grammatical errors. Here is a non-comprehensive list:

- An en-dash (not a hyphen, and not an em-dash) should be between words/objects which specify a pair: enhancer–target gene, enhancer–promoter, variant–promoter
- “megabase pairs” should be “mega basepairs” or “mega base-pairs” (L220)
- “complied” should be “compiled” (L278)
- “tetails” should be “details” (L363)

Additionally, there are areas which could use more clarity

- In the tables comparing performance between the models, because the expert model is effectively always by far the best one, it would be useful to underline the second-best model, as well (or use another way to emphasize the second-best model in addition to the best)
- In Table 2, the shape of the output in contact-map prediction is a bit confusing, as contact maps are typically thought of as 2D objects rather than a single 99681-vector
- The order of the datasets/tasks is not the same in the Table 2, the main text, and the supplement in different sections; there doesn’t seem to be a reason why the ordering of these 5 tasks can’t be presented in the same ordering each time
- In the data repositories at `https://dataverse.harvard.edu/`, it is not clear what each file represents and how the data is organized *vis a vis* the descriptions in the appendix; a README should be added to each repository

### Questions
1. What is the stratified sampling approach used in some of these tasks (i.e. enhancer–target-gene prediction, eQTL prediction); that is, what is the stratification based off of?
2. In any of these datasets/tasks, is it possible that the same genomic coordinate appears in multiple dataset splits (e.g. train and test)? This could be possible if the examples arising from the same gene end up in different splits, for example
3. When masking out other enhancers in the enhancer–target-gene task, what were these enhancers masked with?
4. What was the reasoning for removing genes with too few positive/negative pairs (i.e. enhancer–target-gene prediction, eQTL prediction)?

### Soundness
3

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
4

### Summary
The paper proposes DNALongBench, a new benchmark for genomic tasks that consider long-range dependencies of up to 1 million base pairs. The benchmark provides five tasks, enhancer-target gene interaction, expression quantitative trait loci, 3D genome organization, regulatory sequence activity, and transcription initiation signal, with different requirements. The authors evaluate five models per task, including a task-specific expert model, a CNN baseline and three DNA foundation models. The authors claim that DNALongBench is the most comprehensive benchmark tailored to DNA long-range tasks to date.

### Strengths
- The paper studies a significant problem in computational biology. DNA regulation and Chromatin structure appears to be one of the challenges in the field and improvements could lead to novel insights into gene regulation and cellular regulatory networks.

- The paper is well-written and well structured.

- The effort of collecting data from different sources, curating the data, and providing it for download is a strong part of the work.

- Each individual task, the biological importance, the data, and evaluation is well-described. The authors seem to be well informed about the literature and the underlying problem.

### Weaknesses
Major:

1. It is unclear to me how many of the tasks really require long context to achieve strong results. 

2. A clear limitation of the work, which is also stated by the authors in the conclusion, is that they do not evaluate transformer based models on the different tasks.

3. The codebase is not well documented, there is only a readme and one line referring to a notebook with code for the dataloaders.  

Please see more explanations below.

Regarding 1:

Some overview tables/plots in the appendix that clearly show the long-range dependencies of the tasks would make sense I think.


Regarding 2:

While it makes sense that models for genomic data require long contexts, the argument of *NOT* training attention-based models appears weak. The authors use a CNN baseline which obviously does not have a receptive field spanning millions of tokens / base pairs. However, even this “lightweight” baseline seems to outperform the foundation models in some of the tasks (see e.g. Table 4 RSAP Human and Avg, Table 5 WB, SNSES, MS). I would rather say that models with limited context size would be very useful to argue in favor of the development of a long-range benchmark if they really perform worse than non-attention based FMs. Otherwise, the benchmark might still add value, but probably the line of argumentation should be different.


Regarding 3:

I think a benchmark should seamlessly integrate with developer code for a new method to be useful in practice. The authors state that they envision that DNALongBench could be a valuable resource for future evaluations, however, this requires clear documentation, a user friendly interface, and in the best case a leaderboard. A benchmark should integrate into my own codebase with only a few lines of code but it seems like I would have to integrate my code into DNALongBench instead. This clearly limits the usability of DNALongBench and I strongly recommend that the authors work on their code base.

For example, an API as follows would be very helpful to increase the usability

```
import myModel
import Benchmark

benchmark = Benchmark(task=’someTask’)
model = myModel()

def prediction_wrapper(task):
    prediction = model.inference(task.x)
    return prediction

results = benchmark(prediction_wrapper)

print(results)
```
The provided dataloaders might be useful, however, I'm missing a clear description and interface for the evaluation.
Overall, the lack of documentation is an important weakness here. While the API could still be improved until the CRC deadline, I hope the authors can already show some improvements during time of rebuttal.  

For a good example benchmark see e.g. [1] (featured paper at NeurIPS 2022 DBT)

Minor: 

Line 363 typo: tetails -> details

Line 303: Maybe I missed it but SNPs are not introduced.

Line 479: Additional the

### Questions
See also weaknesses.

- How much of the tasks really require long-range interaction predictions?
- How do attention-based models perform on the tasks?

### Soundness
3

### Presentation
3

### Contribution
2
