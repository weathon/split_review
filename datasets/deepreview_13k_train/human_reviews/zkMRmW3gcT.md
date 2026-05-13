# Elucidating the Design Space of Language Models for Image Generation

- Decision: Reject
- Scores: 5, 5, 3, 6, 5

## Abstract
The success of autoregressive (AR) language models in text generation has inspired the computer vision community to adopt Large Language Models (LLMs) for image generation. 
However, considering the essential differences between text and image modalities, the design space of language models for image generation remains underexplored. 
We observe that image tokens exhibit greater randomness compared to text tokens, which presents challenges when training with token prediction.
Nevertheless, AR models demonstrate their potential by effectively learning patterns even from a seemingly suboptimal optimization problem.
Our analysis also reveals that while all models successfully grasp the importance of local information in image generation, smaller models struggle to capture the global context. In contrast, larger models showcase improved capabilities in this area, helping to explain the performance gains achieved when scaling up model size.
We further elucidate the design space of language models for vision generation, including tokenizer choice, model choice, model scalability, vocabulary design, and sampling strategy through extensive comparative experiments. Our work is the first to analyze the optimization behavior of language models in vision generation, and we believe it can inspire more effective designs when applying LMs to other domains. Finally, our elucidate language model for image generation, termed as \textbf{ELM}, achieves state-of-the-art performance on the ImageNet 256$\times$256 benchmark.git}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper investigates the application of language models for vision generation tasks by exploring differences between image and text token distributions, the training dynamics of autoregressive models versus masked language models (MLMs), and the efficacy of different image discretization approaches. The authors propose a new model, ELM (Elucidated Language Model for Image generation), which combines AR modeling with Binary Autoencoder (BAE) for discretization. Key insights include the advantage of AR models for capturing image structures, the benefits of BAE in reducing computational costs and improving performance, and the ability of AR models to learn effective image patterns without inductive biases.

### Strengths
The paper examines different components of language models in image generation, such as tokenization methods, model scalability, and sampling strategies, providing insights into optimizing language models for visual tasks.

The ELM model integrates binary autoencoders for effective tokenization and AR models for scalability and performance. Extensive experimentation validates the authors' design choices, as ELM achieves high performance across various model sizes.

### Weaknesses
While the paper positions ELM as an alternative to diffusion models for image generation, more direct comparisons with these models could strengthen the evaluation. How does ELM compare in performance and efficiency to diffusion models in a similar setting?

While the study uses ImageNet as a benchmark, it doesn’t explore a broader range of datasets or domains that might reveal limitations in model generalization. How might the model’s performance be affected by training on datasets with higher resolution images or more complex scenes than ImageNet provides.

How robust is ELM in scenarios requiring conditional generation with complex prompts or context?

### Questions
Could the proposed design principles for image generation apply to other visual tasks, such as video generation?

How does the model handle diverse visual patterns, such as textures or irregular structures, compared to more common AR or diffusion models?

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
3

### Summary
In this work, the authors investigate the effects of different modeling choices for using language models for image generation. Specifically, they compare two tokenizers (VQGAN and BAE), two loss functions (AR and MLM), vocabulary designs, and different sampling strategies. Based on this exploration, the authors propose the ELM model and achieve strong performance on the class-conditional ImageNet 256X256 image generation task when compared with competitive AR baselines.

### Strengths
1.	Research questions proposed by this paper, i.e. how to design language models for image generation, is a very timely and important subject to investigate. 

2.	This paper presents substantial efforts in searching for better alternatives compared to the dominating tokenization approach that uses a pretrained VQGAN model. 

3.	Their proposed ELM achieves SOTA performance on class-conditional ImageNet 256X256 image generation.

### Weaknesses
While this paper explores an important research direction, the attempt is nevertheless lacks rigor and stronger experimental validation. Specifically, my main concerns include the following: 

1.	Failure to compare with continuous-valued tokenization: As the most competitive baseline shown in this paper, MAR, which uses continuous-valued tokenization, achieves very comparable performance (FID 1.55) in comparison to ELM (FID 1.54). However, the authors did not include continuous-valued tokenizers in their design space.

2.	Failure to compare with masked autoregressive loss: Similarly, MAR uses masked autoregressive loss, which is also not included in their design space. 

3.	Unconvincing comparison with MAR: Note that MAR  achieves almost identical performance as the best performing ELM with only half of the parameter size. And when comparing the two models with similar parameter size, MAR shows very clear advantages over ELM. This shows the minor improvement that ELM brings – especially with the discussion of scaling laws, one can imagine scaling up MAR further can potentially also improve the performance, and therefore MAR can potentially outperform ELM if scaled up to 2B parameter size.

4.	Failure to explore the effect of token orderings and token types: Even if the authors intend to only compare discrete tokens, they have missed several comparison points such as the ordering of the tokens (e.g. scanline, zig-zag, etc) and the types of the tokens (e.g. image patches, image scales, etc). These design choices are arguably equally important and underexplored as the ones presented in the paper. 

5.	Contradicting discussions and conclusions: In Section 3.1, the authors noted that training loss is not a good indicator for the model performance. However, in later sections, e.g. when analyzing the scaling laws, the authors still use the training loss as the metric for evaluation. 

6.	A few claims: 
a.	In Section 3.1, the authors claim that “image data lacks the inherent structure” from their KL divergence analysis with uniform distribution. Not only does this analysis have no connection to the conclusion, the claim itself is also invalid without further assumptions (e.g. [1]). If the authors had explored different token types (e.g. the scale tokens), they may also observe different divergences and may reach different conclusions.
b.	In Section 3.4, the authors use the visualized attention maps to study the ability to learn global v.s. local information. However, this kind of visualization does not necessarily accurately reflect the actual functionality of the network according to [2]. 

7.	Failure to explore the combinatorial design space: The authors fix the tokenizer choice when comparing different loss functions, tokenization designs and sampling strategies. However, they fail to consider the combinations of these choices with the other tokenizer choice. For example, it is possible that VQGAN tokens + MLM behaves differently with AR and MLM, or even potentially performs better than BAE tokens + AR. Given that VQGAN is a popular choice for many AR image generation models, it would be valuable to analyze behaviors with VQGAN tokens.

A few minor suggestions:  
1.	Line 164, the notation of the conditional probability is very confusing and not conventional
2.	Almost all plots have fonts that are too small and therefore hard to read

### Questions
It would be great if the authors can address the weakness mentioned above, especially a more thorough discussion and comparison with MAR.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates the design space of image generation using language models, whose space includes the type of image tokenizer (e.g., vector-quantized or binary-value quantized auto-encoders, decomposition), type of language model (e.g., autoregressive or masked language model), scaling behavior (e.g., learning vs model sizes, vocabulary size vs model size). With extensive study, the paper suggests an optimal combination of design choices, leading to a strong image generation performance on class-conditional image generation on 256x256 ImageNet, whose performance is on par with existing state-of-the-art methods.

### Strengths
* The paper has clearly laid out some important design choices of building language model based image generation model. The recipe provided in this paper could be useful to the community.

### Weaknesses
 * Overall, I didn't find the findings of the paper new, surprising, or significant over those from previous works.

* The design space elucidated in this paper is mostly from existing works. While it is great that the paper has compiled them into a single paper, the contribution is very limited by nature. Furthermore, the optimal design choices made in this paper is not very different from the previous findings, which limit the contribution of the paper to confirm what is already known.

  * Section 3.2 Tokenizer choice: VQGAN vs BAE is repetition of the study conducted by previous work [Yu et al., 2024]
  * Section 3.5 Vocabulary design has been studied in [Yu et al., 2024] (Section 3.1, paragraph "Token factorization for efficient prediction") and confirmed decomposition into two subcodes being generally optimal.

* Section 3.1 Image generation vs text generation, which compares the property of image and text tokenizers, does not seem rigorous and conclusive.
  * In Table 1, how is "bigram" distribution obtained from the image tokens? Specifically, how is "consecutiveness" defined? Raster-order?
  * Token distribution analysis seems misleading. For example, the sentence in line 216 "the randomness in image token distribution implies that image generation doesn't depend on strict sequential patterns" is not well justified. Unigram distribution being uniform only suggests that the frequency of items in vocabulary is uniformly distributed, but it is unclear how unigram distribution could imply anything about the sequential pattern.
  * Ultimately, what is the take-home message of this section? Image and text tokenizers have different distribution and image tokenizer seems to have more randomness, so it is more difficult. And? What design choice consideration should we be making knowing that the difference in distributions?



### Questions
Please see weakness section for more context.

* What are new findings from Section 3.2 and 3.5 compared to [[Yu et al., 2024](https://arxiv.org/pdf/2310.05737)]?
* Regarding Section 3.1:
  * In Table 1, how is "bigram" distribution obtained from the image tokens? Specifically, how is "consecutiveness" defined? Raster-order?
  * The sentence in line 216 "the randomness in image token distribution implies that image generation doesn't depend on strict sequential patterns" is not well justified. Unigram distribution being uniform only suggests that the frequency of items in vocabulary is uniformly distributed, but it is unclear how unigram distribution could imply anything about the sequential pattern.
  * Ultimately, what is the take-home message of the section 3.1? Image and text tokenizers have different distribution and image tokenizer seems to have more randomness, so it is more difficult. And? What design choice consideration should we be making knowing that the difference in distributions?

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
This paper conducts a thorough analysis on the use of LMs for image generation. This approach usually involves two stages: (1) training an image quantizer to convert image patches into discrete tokens and (2) training a language model to model this token distribution. While this approach is not new, this paper dives deeper into the design choices used in this generation setup, providing insights into the architectural and hyperparameter choices that influence this regime. They demonstrate strong results on ImageNet generation.

### Strengths
- The paper explores many different dimensions of the LM setup, ablating across both the stage 1 tokenizer and the stage 2 LM.
- Section 3 of the paper provides nice visualizations and sheds some light on how LMs learn the image generation task (which is not entirely intuitive, especially for the autoregressive nature).
- This paper explores autoregressive generation, which has distinct advantages over diffusion models (for example, leveraging LLM infra and systems advances). Diffusion models have been the primary focus of the image generation community as of late, so further exploration into this paradigm is valuable.

### Weaknesses
 - The evaluation results are only on 256px ImageNet images, which is saturated at this point. It would be more valuable if the results could be demonstrated on a different task, e.g., text-to-image generation on MS-COCO, or at least on other conditional generation datasets (e.g., CelebA or FFHQ). This would also ensure that the findings transfer to other datasets/tasks.
- The paper suggests that ELM can be used to generate any size images, but there doesn’t seem to be evaluations done at higher resolutions. How does the model compare to 512px images, for example? Is it significantly better to use ELM to generate at 512px, compared to resizing 256px generated images?
- All of the ablations are conducted on model architectures, but recent trends in deep learning suggest that data is more important than architecture. How do the LM models compare against diffusion models in terms of data efficiency/scale? This would be a valuable ablation to run, to find out if either model is more data efficient, or if either LM or diffusion models are better at small data regimes.

### Questions
- How does the inference speed of ELM compare to that of diffusion models?
- Will the models/code be open sourced?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This explores the potential of adapting autoregressive (AR) language models for image generation tasks and study its design spaces. The study investigates how these models can be optimized for image generation, considering the differences between text and image data. The authors identify key challenges, such as the greater randomness in image tokens compared to text tokens, which complicates the training process.

A key focus of the paper is on analyzing the design space of language models for vision generation, including choices in tokenization (e.g., VQGAN vs. BAE), model scalability, and vocabulary design. Through extensive experiments, the authors find that BAE-based tokenization outperforms traditional vector-quantized approaches, and that AR models exhibit better scalability and image generation capabilities than masked language models (MLMs). The study also highlights the importance of model size, showing that larger AR models are better at capturing global context, while smaller models struggle with this aspect.

The main contribution is a comprehensive analysis of the design space for applying language models to image generation. The authors propose the Elucidated Language model for iMage generation (ELM), which achieves state-of-the-art performance on the ImageNet 256×256 benchmark. This work aims to inform future designs of language models for visual content creation and multi-modal inference.

### Strengths
The paper studies the fundamental differences between the token distributions of discretized images and text. Which is an interesting direction.

The paper demonstrate the effectiveness of AR models and its potential on image generation on  the ImageNet 256×256 benchmark.

### Weaknesses
The paper is not presented well and very empirical. I would suggest skip introducing too much details about preliminary works such as VQGAN, BAE without sharing insights designing them for image generation.

The main part of the paper is mainly about experimental comparisons but there are not comprehensive experiments made to support the claims.

Only image quality is reflected in figures such as Figure 8, I would suggest also adding text prompts and also possibly give more complex cases to compare the language understanding ability of autoregressively based LM for visual generation.

The fonts are too small in figure 4,5,6,7.

Only AR models are used as baselines in this paper.

### Questions
Overall, what do you think is the best strength of using LLM for visual generation than diffusion models?

For the tokenizer selection, have you considered using the VAE?

### Soundness
3

### Presentation
2

### Contribution
3
