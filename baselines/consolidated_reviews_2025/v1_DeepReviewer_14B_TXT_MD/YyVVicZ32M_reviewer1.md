### Summary

This paper proposes a new decoding method called Permute-and-Flip (PF) decoder, which has better quality-stability tradeoff than sampling. The authors also design a cryptographic watermarking scheme for PF decoder. The experimental results show that PF decoder outperforms sampling in terms of perplexity, and the watermarking scheme allows for low false positive rate and high recall.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The authors propose a new decoding method called Permute-and-Flip (PF) decoder, which has better quality-stability tradeoff than sampling.
2. The authors design a cryptographic watermarking scheme for PF decoder, which allows for low false positive rate and high recall.
3. The paper is well-written and easy to understand.

### Weaknesses

#### Some Related Works


#### comment

1. The experimental results are not very convincing. The authors only provide results on two datasets and one model. More experiments on different datasets and models are needed to verify the effectiveness of the proposed method. Specifically, the paper lacks a diverse range of datasets that would demonstrate the generalizability of the PF decoder. The current datasets may not fully capture the range of linguistic structures and complexities that the model might encounter in real-world scenarios. Furthermore, the experiments are limited to a single model architecture, which makes it difficult to assess whether the observed improvements are specific to that model or if they can be generalized to other architectures. It is crucial to evaluate the method on a variety of model sizes and architectures to ensure its robustness.
2. The comparison with other decoding methods is not very comprehensive. The authors only compare with sampling and Gumbel WM. More comparisons with other decoding methods are needed to show the superiority of the proposed method. The paper should include comparisons with other state-of-the-art decoding methods, such as beam search, top-k sampling, and nucleus sampling. These methods have different characteristics and trade-offs, and a thorough comparison would provide a more complete understanding of the advantages and disadvantages of the proposed PF decoder. The current comparison is insufficient to establish the superiority of the proposed method over existing alternatives.

### Suggestions

To address the limitations in the experimental evaluation, the authors should significantly expand the range of datasets used for testing the PF decoder. This should include datasets with varying linguistic characteristics, such as those from different domains (e.g., scientific text, news articles, social media posts) and different languages. Furthermore, the experiments should be conducted on a variety of model architectures and sizes, including both smaller and larger models, to demonstrate the scalability and generalizability of the proposed method. It would also be beneficial to include datasets that are specifically designed to test the robustness of the decoder, such as those with noisy or adversarial inputs. This would provide a more comprehensive assessment of the method's performance under different conditions. The authors should also consider reporting results on metrics beyond perplexity, such as BLEU score for translation tasks or ROUGE score for summarization tasks, to provide a more complete picture of the method's effectiveness.

In addition to expanding the dataset and model variety, the authors should also conduct a more comprehensive comparison with other decoding methods. This should include a detailed analysis of the trade-offs between the PF decoder and other methods, such as beam search, top-k sampling, and nucleus sampling. The comparison should not only focus on perplexity but also on other metrics, such as computational cost, diversity of generated text, and sensitivity to hyperparameters. It would be beneficial to include a theoretical analysis of the proposed method, comparing its properties to those of other decoding methods. This would provide a deeper understanding of the method's strengths and weaknesses and help to identify the scenarios in which it is most likely to be effective. The authors should also consider including a discussion of the limitations of the proposed method and potential avenues for future research.

Finally, the authors should provide a more detailed analysis of the watermarking scheme, including its robustness against various attacks, such as paraphrasing, translation, and compression. The current evaluation of the watermarking scheme is limited, and a more thorough analysis is needed to demonstrate its practical applicability. The authors should also consider comparing the proposed watermarking scheme with other existing watermarking techniques, to show its advantages and disadvantages. This would provide a more complete understanding of the method's effectiveness and its potential for real-world applications.

### Questions

1. Are there any plans to conduct more experiments on different datasets and models to verify the effectiveness of the proposed method?
2. Are there any plans to compare the proposed method with other decoding methods to show its superiority?

### Rating

5

### Confidence

3

**********
