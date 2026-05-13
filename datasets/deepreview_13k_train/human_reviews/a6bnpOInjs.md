# Textbook Consistency Weighted Internet Improves Efficiency Twofold

- Decision: Reject
- Scores: 8, 6, 5, 5

## Abstract
We propose a novel method, Textbook Consistency, to improve the training efficiency of large language models by leveraging textbooks as a guiding signal for learning from internet-scale data. Rather than relying on hard filtering of data based on quality thresholds before training, our approach adaptively adjusts the weight of data during training based on its consistency with textbooks during training. We compute the cosine similarity between internet data and textbooks in a latent space, using this metric to modulate the cross-entropy loss. Our method significantly enhances training efficiency, achieving twice the effectiveness by reducing training time or the number of tokens required. Empirical results show superior performance on language models trained on large datasets like FineWeb and The Pile, with extensions to other domains such as robotics. Our method is simple to implement, incurs no additional overhead, and is compatible with existing data curation techniques.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a new method for better (pre-)training of large
language models.

1.  It re-weight each training example (from a large-scale internet
    corpus) based on its embedding similarity with samples from a
    high-quality "text-book" like corpus.

2.  Authors find that the method can train language models more
    efficiently (achieving the same loss with less compute) or more
    effectively (achieving lower loss with the same compute) with
    experiments of 375M, 1.2B, and 3B llama models on the fineweb and
    the pile datasets.

3.  The author additionally shows that the method can be applied to
    other domains like robotics with experiments on the ExoRL dataset.

### Strengths
Overall the paper is well-written with nicely presented results, the
method is simple and intuitive, and the experiments are properly
designed and executed.

1.  I like the idea of using textbooks as a guiding signal for training,
    which can potentially remove low-quality samples from the
    large-scale web data and improve the training. Typically, people
    have to manually create "hard" heuristics to filter samples and mix
    data based on a lot of experiments and ablations. To some extent,
    this method *automatically* creates such "soft" heuristics, which is
    a nice idea.

2.  The method itself is easy to execute and I think it can be easily
    integrated into existing training pipelines. The experiments are
    well-designed and the results seem to be convincing. It's also
    simpler to implement than other curriculum learning-based methods.

### Weaknesses
I generally like this paper; here I add some additional comments and
thoughts that could further strengthen the paper.

I think the author proved that the method can improve the training, but
it seems one possibility is that the method can make the learning more
"strategic and focused" by increasing the weight of samples that are
more similar to the textbook guidance (which is similar to the test data
in some sense). This could cause some unintended consequences like
reducing the diversity of the generations or not being able to learn the
long-tail knowledge. I do not think the current experiments can show the
method can avoid/cause these issues. (And the explanation in takeaway
(line 355) seems to support the strategic learning hypothesis as I see
larger drop on maths/abstract given the text guidance contains
MetaMathQA examples.)

### Questions
1.  line 175: can you provide more details about the computation of the
    FLOPS (The computational cost (FLOPs) incurred by the embedding
    model is less than 0.5% of the total training FLOPs, even for the
    smallest 375M model)?

2.  line 323: \"while the blue bars represent models that incorporate
    consistency\" blue seems to be a typo (or the figure is not right)?

3.  line 377: \"evaluate its impact on validation loss and how each
    variant performs against a baseline\" what is the baseline?

4.  figure 5: for y axis, what's the direction of time progression (from
    top to bottom or bottom to top)?

5.  section 3.3: how is the similarity computed in the RL setup? What
    are the details of the training? Please provide more details.

6. will the code be released?

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
3

### Summary
In this work, the authors introduce a training-effective method called Textbook Consistency. This method improves the training phase by utilizing high quality textbook datasets to align and improve the relatively lower-quality training internet data. Subsequent experiments demonstrate the efficiency of this method. Additionally, the authors successfully generalize this approach to robotic tasks.

### Strengths
- The authors propose an effective training method called textbook consistency. It can successfully enhances training performance with minimal additional cost.
- The authors conduct a variety of experiments that support the effectiveness of textbook consistency.

### Weaknesses
 - The presentation could be improved. The authors should refine the captions for Fig 3, Fig 4, Tab 1, and Tab 2, by providing necessary information such as the size of the tested models in Figure 4 and Table 1.
- Comparing validation loss across models of different sizes seems unhelpful. Additionally, the meaning of "2x" in Fig 3 is unclear since the x-axis represents parameters.
- More downstream tasks, like MMLU and GSM8K, should be included. A slight improvement in loss may not effectively impact real-world performance. Furthermore, the comparison between "Internet" and "Internet + Textbook" might not be fair due to the inclusion of instruction tuning format training data in the textbook.
- The experiments on robotic tasks appear somewhat disconnected. It would be better for the authors to focus more on language-based tasks.

### Questions
- How the selection of embedding models impacts training performance, given that BERT-base is a weaker embedding model compared to state-of-the-art options.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces "Textbook Consistency," a training method to enhance the efficiency of large language models (LLMs) by dynamically weighting internet data based on its alignment with high-quality, textbook-based sources. Unlike traditional data filtering, which discards or retains data based on fixed quality thresholds, this method computes cosine similarity between internet data and textbook sources to continuously adjust data weighting. This approach reduces training requirements, either by cutting training time or the number of tokens needed, thereby doubling efficiency without added computational burden. Empirical results indicate superior model performance on extensive datasets and applicability across domains, including robotics.

### Strengths
1. The method is computationally efficient and straightforward to implement, aligning with current data curation methods. Adaptively adjusting data weights reduces the need for extensive filtering, making training faster and more adaptable. 

2. The technique proved versatile, demonstrating improved performance across both language and robotics tasks.

### Weaknesses
1. During training, the weight of internet data in the current batch depends exclusively on the similarity with the current batch textbook, which could intuitively introduce additional bias and may hinder the accurate evaluation of sample quality.

1-1. This study is similar to research on dynamically adjusting learning rates; however, it is not discussed in the related work. Could an explanation be provided to clarify the difference between this approach and research on dynamically adjusting data recipes [1,2]?

1-2 Above that, for greater persuasiveness, the experiment could include a comparison with training data selected by the proxy model.

2. The experimental setup is unconventional; repeated training with the textbook data could lead to overfitting. While Figure 2 suggests that the proposed method helps alleviate overfitting, would it not be more reasonable to compare the results of training the "internet data" alone with the “Textbook Consistency” method?

3. Evaluating only based on validation loss may be insufficient. Would it be possible to incorporate additional downstream tasks for assessment, such as MMLU, ARC, and other general benchmarks? Considering the so huge cost of pre-training, further pre-training could be incorporated to assess how effectively the current method enhances the pre-trained model, with additional improvement on a pre-trained model better demonstrating the study's contribution.

### Questions
See weakness.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
## Summary
The paper presents a method to train LLMs efficiently by assigning (dynamic) weights to training data. The paper claims this improves training efficiency by a factor of atleast 2, as it needs less data to achieve same performance (read validation loss)

## Contributions
1. Authors demonstrate that not all internet training data is equal, and comparing this data with known high quality data can improve training efficiency
2. Paper also demonstrates that we need both highly curated (read textbook) and internet scale data

### Strengths
1. Detailed ablation study highlighting importance of using both textbook data and internet data
2. Ablation on impact of parameter size on model
3. Evaluation on downstream tasks

### Weaknesses
1. I have major concerns regarding the experimental setup -- especially the dynamic nature of weights defined in the paper which signifies importance of an internet sentence. The paper claims the weights are dynamic, but the embedding model used to compute the embedding 'e' is fixed. This means that for a given internet sentence, the embedding will always be the same, and hence the weight will always be the same. This is a major flaw in the methodology.
2. I am also not convinced how two random sentences give an indication that internet sentence is important or not. The method uses a random sentence from a textbook to compare against an internet sentence. This comparison is then used to assign a weight to the internet sentence. It is highly likely that two randomly selected sentences will have very little semantic overlap, leading to weights that do not accurately reflect the true importance of the internet sentence. The paper does not explore alternative methods for determining sentence importance, such as using a sentence similarity metric based on contextual embeddings or a more sophisticated matching algorithm.



### Questions
1. Line 130 claims that e comes from either an embedding model (which is fixed) or the model itself. How is the weight ``dynamic`` when ``e`` is fixed? Won't w_i be same? Can't you compute this before you even start your training? This is also mentioned in Line 161 where you describe your training setup
2. Another major concern is regarding how you compute importance of an internet sentence. You randomly select some sentences from textbooks to compute importance of internet sentence. Won't this value almost always be close to -1 (as you are comparing complete random sentences, and any two random sentences should be unrelated right?). Perhaps an approach which searched for best sentence match from textbook corpus work better? Or atleast used as a baseline
3. How is the validation loss reported throughout the paper (Figure 2, 3, Table 1...) computed? Is it NLL (Line 105) or the weighted NLL (Line 134)
4. What is the size of validation data used in Figure 2?
5. What exactly does fillering mentioned in Lines 402-404 mean? Is the data which does not lie within the threshold filtered out?

### Soundness
2

### Presentation
2

### Contribution
2
