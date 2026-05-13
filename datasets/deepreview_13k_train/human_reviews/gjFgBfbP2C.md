# NeuralMark: Advancing White-Box Neural Network Watermarking

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
As valuable digital assets, deep neural networks require ownership protection, making neural network watermarking (NNW) a promising solution. In this paper, we propose a *NeuralMark* method to advance white-box NNW, which can be seamlessly integrated into various network architectures. NeuralMark first establishes a hash mapping between the secret key and the watermark, enabling resistance to forging attacks. The watermark then functions as a filter to select model parameters for embedding, providing resilience against overwriting attacks. Furthermore, NeuralMark utilizes average pooling to defend against fine-tuning and pruning attacks. Theoretically, we analyze its security boundary. Empirically, we verify its effectiveness across 14 distinct Convolutional and Transformer architectures, covering five image classification tasks and one text generation task. The source codes are available at https://anonymous.4open.science/r/NeuralMark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a white-box neural network watermarking method NeuralMark, which aims to protect the network from three typical attacks. To offer resistance to forging attacks, NeuralMark establishes a hash-based mapping between keys and watermarks. It selectively embeds watermarks into model parameters to counter overwriting attacks and uses average pooling to defend against fine-tuning and pruning. The security and effectiveness of the method have been empirically verified on multiple architectures and various tasks.

### Strengths
- Comprehensive experiments demonstrate the scalability of the proposed NeuralMark across 14 models, covering five image tasks and one text generation task.
- The paper provides a theoretical analysis to determine the security boundary.

### Weaknesses
 - The paper lacks consideration for the adaptive attack, which are crucial for robustness. A naïve adaptive attack can freeze model parameters and minimize the $L_e$ loss to learn the key and watermark, potentially compromising model ownership. The paper should explore scenarios where an attacker iteratively refines a forged watermark and key by observing the detection response, which is a more realistic threat model than simply generating random forgeries.
- The paper lacks a detailed description of attack methods, particularly whether fine-tuning and pruning are applied to all parameters or only the Watermark Filtering layer. This is critical because the resilience of the method could be significantly affected if attacks are limited to only the watermark embedding layer, which might not represent a realistic attack scenario. For example, if fine-tuning only affects the watermark layer, the attacker might not be able to degrade the primary task performance, thus limiting the attack's effectiveness.
- The resistance to overwriting attacks for NeuralMark is unclear. In Section 5.3, the “Overwriting Attack” paragraph states that “the adversary’s watermark detection rate reaches 100%”, which, even if matched by the original watermark, still leaves model ownership ambiguous. The paper needs to clarify how the method can differentiate between the original watermark and a forged watermark that also achieves a 100% detection rate, especially in cases where the attacker has access to the model parameters.
- Limitations of the proposed method are not explicitly discussed. The paper should address the scenarios where the method might fail or be less effective, such as when the model is deployed in a black-box setting where parameter access is restricted. This is crucial for understanding the practical applicability of the method.
- Experimental comparisons with other methods are insufficient. For instance, in Figure 3, only resistance to pruning attacks at various ratios is shown for NeuralMark without comparisons to other methods. Additionally, Table 5 only compares against VanillaMark, lacking comparisons with GreedyMark. The paper needs to include comparisons with other state-of-the-art watermarking techniques to provide a comprehensive evaluation of the proposed method's performance.

### Questions
- Can the proposed method defend against adaptive attacks? Additional experiments to assess its resilience to adaptive attacks are necessary.
- How are the three types of attacks applied? Are fine-tuning and pruning applied to all parameters, or only to the Watermark Filtering layer? If the latter, would the method still be effective against attacks?
- Can this method resist overwriting attacks? With both the original and adversarial watermark detection rates at 100%, there is ambiguity in model ownership.
- What are the limitations of NeuralMark?
- Can the experimental comparisons with other methods be expanded? For example, comparative experiments with other methods need to be added in Figure 3 and Table 5.

### Soundness
3

### Presentation
2

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
The paper introduces NeuralMark, a white-box watermarking method aimed at safeguarding the ownership of deep neural networks by embedding robust watermarks that resist various attacks. NeuralMark employs a three strategies: a hash mapping links a secret key to the watermark, serving as a defense against forging; watermark filtering secures the model parameters from overwriting; and average pooling protects against fine-tuning and pruning attacks.

### Strengths
1. NeuralMark integrates hash mapping, which ties the secret key directly to the watermark, thus significantly reducing vulnerability to forgery. This approach makes reverse engineering infeasible by adversaries, as altering the watermark would require breaking the hash.

2. Watermark filtering limits parameter overlap, making overwriting attacks more challenging. This filtering method ensures that even if adversaries attempt to embed a new watermark, the likelihood of interference with the original watermark is minimized.

3. Tests conducted on diverse datasets (e.g., CIFAR, TinyImageNet, and Caltech) show that NeuralMark imposes minimal accuracy loss, indicating that it balances watermark robustness and model fidelity effectively​.

### Weaknesses
1. The motivation is unclear. Although the authors explain the motivation for the design of the scheme, they do not explain why they are interested in weight-based watermarking. In the introduction, the author introduces three types of model watermarking techniques and states that all three types of watermarking techniques face the same attacks. It is strange and incomprehensible that the author flatly promotes that they only focus on model weight-based watermarking techniques without clearly comparing the pros and cons of the three types of techniques.

2. The references do not take into account the latest research progress. The introduction of weight-based methods in Related Works only covers work up to 2021. I don't believe there has been no new progress in this direction in the past three years. In addition, in the experimental comparison, only two old solutions were compared, one proposed in 2017 and the other proposed in 2021. There is no comparison with the SOTA solutions, which makes the experimental results unconvincing.

3. This paper says that performing the filtering round more times can reduce the overlap ratio, but it also reduces the number of weight parameters for embedding the watermark. Will this affect the security of the watermark? It is necessary to conduct an experimental analysis.

4. The details of fine-tuning attacks are known.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces NeuralMark, a method for white-box neural network watermarking to protect ownership. It integrates seamlessly into various network architectures, using hash mapping, watermark filtering, and average pooling to enhance security against forging, overwriting, fine-tuning, and pruning attacks. NeuralMark is empirically validated across 14 different architectures and multiple tasks, demonstrating its effectiveness while maintaining model performance and security.

### Strengths
- The research direction about model watermarks is important. As deep learning is driven by the scale, more and more resources have been invested in designing and developing deep models, and therefore ownership protection methods are necessary for safeguarding these models of interests.
- This paper extended model watermarks to the Transformer architecture, while previous work didn't. Empirical results on Vision Transformers,  GPT-2 and Swin Transformers demonstrate the effectiveness of the proposed method.
- The presentation is clear and in general well-written.

### Weaknesses
 - The proposed method seems to be incremental. I am aware that there are some numerical improvements in the reported results. However, no substantial contribution to watermark design, in the aspects of robustness or fidelity for example. 
- Further results on ambiguity attacks (i.e., attacks that would cast ambiguity over the verification process, including forging attacks and overwriting attacks) are needed. See below for details.

- To my understanding, the proposed algorithm is public while the watermark (i.e., the specific parameter filter in the proposed method) is secret, according to Kerckhoff's Principle. After preliminary verification, the watermark is also publically available, and since the adversary also knows the hidden watermark, what happens to the next verification process? After the first verification, anyone knows the embedded watermark and anyone also could claim ownership, which may cast ambiguity over the verification process after the first verification. In other words, can the proposed method support public verification?

### Questions
- To my understanding, the proposed algorithm is public while the watermark (i.e., the specific parameter filter in the proposed method) is secret, according to Kerckhoff's Principle. After preliminary verification, the watermark is also publically available, and since the adversary also knows the hidden watermark, what happens to the next verification process? After the first verification, anyone knows the embedded watermark and anyone also could claim ownership, which may cast ambiguity over the verification process after the first verification. In other words, can the proposed method support public verification?
- For the above question, I think one possible solution is to map the owner's signature to the watermark binary code, e.g.,  [1, 0, 1, 0]. If so, I would suggest additional analyses and ablation studies about the binary code design in the experiment section.
- Will the source codes and datasets with necessary documents and instructions be publicly available?

I would raise my rating if these concerns are addressed.

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
3

### Summary
This paper proposes an advanced white-box watermarking technique that defends against watermark removal attacks through average pooling, establishes a key-to-watermark hash mapping to defend against watermark forgery attacks, and also enhances watermark privacy by using binarised watermarks as a filter for watermark injection parameter selection.

### Strengths
1. it makes sense to use watermarking by binarisation as a filter for the injected parameters. 
2. the authors provide a theoretical analysis of the security bounds of NeuralMark. 
3. extensive experiments show that NeuralMark can effectively resist watermarking attacks without significantly affecting the model.

### Weaknesses
The authors establish a key-to-watermark hash mapping, but a similar method for establishing a passport sample-to-watermark hash mapping is already available in [1]. Despite the author's citation of the article in [1], the article does not explain the necessity of using keys directly for hash mapping. In addition, to defend against Removal+Forging Attack, the authors use average pooling, which was also proposed in previous articles [2,3]. As a key module to defend against watermark removal attacks, the approach used by the authors does not advance the knowledge in the field of watermarking. The use of average pooling, while effective against some removal attempts, is a relatively straightforward technique and its integration doesn't represent a significant leap in methodology. Furthermore, the paper lacks a detailed discussion on the limitations of average pooling, such as its potential vulnerability to more sophisticated removal attacks that might target the pooling operation itself or employ adaptive strategies to circumvent it. The paper also does not explore alternative or complementary techniques that could enhance the robustness of the watermark against a wider range of removal strategies. The binarized watermark as a filter for injection parameters, while novel, lacks a thorough analysis of its impact on model performance and generalization. The paper does not provide sufficient evidence to show that this filtering mechanism does not introduce any bias or unintended consequences on the model's learning process.

### Questions
Three levels of watermarking attacks are presented in Section 2.3.2. However, the Threat Model in Section 3.3 does not seem to be analysed in conjunction with the levels of watermarking attacks.The Removal+Forging Attack first attempts a watermark removal attack, which belongs to Level II in Section 3.2. This is followed by the Forging Attack. I'm not sure if it becomes more difficult to perform a forging attack on a model that has already had its watermark removed. If the attack is successful, this seems to be just a combination of Level I and Level II. It seems like it would look more reasonable to switch the order of the two attacks.

 For the experiments of watermark removal by pruning in Removal+Forging Attack, the author chooses to carry out the watermark forging attack with 40% pruning rate, combining with Figure3 to see that 40% doesn't seem to be a special turning point, and I'm very curious about the robustness of NeuralMark's other different pruning rates to watermark forging attacks. .

### Soundness
3

### Presentation
3

### Contribution
2
