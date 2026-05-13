# Functional Interpolation for Relative Positions improves Long Context Transformers

- Decision: Accept
- Scores: 8, 6, 6

## Abstract
Preventing the performance decay of Transformers on inputs longer than those used for training has been an important challenge in extending the context length of these models. Though the Transformer architecture has fundamentally no limits on the input sequence lengths it can process, the choice of position encoding used during training can limit the performance of these models on longer inputs. We propose a novel functional relative position encoding with progressive interpolation, FIRE, to improve Transformer generalization to longer contexts. We theoretically prove that this can represent some of the popular relative position encodings, such as T5's RPE, Alibi, and Kerple. We next empirically show that FIRE models have better generalization to longer contexts on both zero-shot language modeling and long text benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes to use a small neural network that computes the positional bias used in self attention. The authors show that such a positional encoding is a generalization of several popular relative position encodings. Importantly, when combined with progressive interpolation (normalizing by the current position), they showcase superior performance in length generalization when using the proposed positional encoding. The authors perform extensive experiments on zero-shot length generalization as well as fine-tuning with longer sequences and show that the proposed method outperforms a host of other positional encodings.

### Strengths
The paper is very well written. The related work is clearly presented as is the proposed method.

Given the simplicity of the contribution, extensive experiments are required to ensure the universality of the proposed positional encoding. The authors perform experiments at two model scales, evaluating zero-shot generalization as well as generalization with fine-tuning. Moreover the authors provide extensive ablation studies for all components of the method.

### Weaknesses
It is not very clear why ALiBi performs so poorly while both in the Kerple paper and ALiBi paper, ALiBi shows great zero-shot length generalization.

Additionally, a simple baseline is missing, namely interpolating a learnable positional bias using $\frac{\psi(i - j)}{\psi(i)}$. This would show whether the nugget of the method is the progressive interpolation or the neural network or both. From the visualization of the learned positional biases the functions learned by the neural network are, as expected, not too complicated.

### Questions
Asked in the weaknesses section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose FIRE: functional interpolation for relative positional encoding. The idea is to first project relative position to a real number between 0 and 1, and this projected number is subsequently fed to a MLP to generate positional bias. FIRE enables language models to train on a short sequence length, and then generalize to longer sequence length during testing. Extensive experiments are conducted to demonstrate the effectiveness of the proposed method.

### Strengths
* The proposed method is very intuitive and easy to understand. The presentation is very clear. The main motivation is that many existing positional encoding methods cannot extrapolate to unseen sequence length, limiting their practicality. The idea of projecting relative positions to a real number between $[0,1]$ is very natural.

* The authors conduct extensive experiments to demonstrate the effectiveness of the proposed method. Models pre-trained with different positional encoding approaches are evaluated under different settings: fine-tuning on long and short context taks, and zero-shot generalization to unseen sequence length.

### Weaknesses
 * Some of the design choices are ad-hoc, especially the thresholding parameter for the normalizer. From Table 3, it seems model performance considerably degrades on short sequence length without this thresholding parameter. I’m wondering about the model performance of using Eq. 21 on GLUE/SuperGLUE.

* Also regarding the thresholding parameter, it is mentioned that the parameter $L$ is learnable. Could the authors demonstrate what the learned parameter $L$ looks like after training? Also, will model performance significantly change if we set $L$ to a fixed value?

* Another weakness is that FIRE is not better than existing methods when the sequence length is short. Even with the thresholding parameter and the slower inference speed, it seems FIRE is not better than RoPE on GLUE/SuperGLUE. Furthermore, the necessity of the thresholding parameter, which seems crucial for short sequence performance, introduces an additional hyperparameter to tune, potentially complicating the practical application of the method.

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Preventing performance degradation of Transformers on inputs longer than the training sequence lengths has posed a significant challenge in expanding the context length of these models. While the Transformer architecture inherently has no limitations on the input sequence lengths it can handle, the choice of position encoding during training can limit their performance on longer inputs. To address this, the author propose a novel approach called Functional Interpolation with Relative Encoding (FIRE), which aims to enhance Transformer's generalization to longer contexts. The author provide theoretical evidence that FIRE can effectively represent popular relative position encodings like T5's RPE, Alibi, and Kerple. Furthermore, The author empirically demonstrate that the FIRE models exhibit improved generalization to longer contexts in both zero-shot language modeling and long text benchmarks.

### Strengths
The author introduces a new relative position encoding and demonstrates its superior extrapolation capabilities.

### Weaknesses
Although the performance of the model presented in this paper is impressive, I believe there are several shortcomings:

1. Heavy reliance on handcrafted input features: The authors attempt to use a neural network to learn a relative position encoding. However, the input features of this network still heavily rely on manual design. Although some ablation experiments are conducted in section B.1, I believe the baseline should be a simpler approach like b(i, j) = f(i - j). For example, [1], [2] has achieved good results by learning relative positional relationships using a similar approach.

2. Trade-off between efficiency and performance: Compared to Alibi and RoPE, the learnable FIRE raises the question of how much slower it makes the training process for language modeling. However, this aspect is not mentioned in the paper. Therefore, the authors need to evaluate and discuss the training speed.

3. Lack of certain baselines: For instance, the paper fails to compare its approach with NTK-RoPE[3], YaRN[4], and NTK-ALiBi[5]. These methods have also made advancements in relative position encoding. The absence of comparison with these baselines is a drawback.

### Questions
The same as weaknesses part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
