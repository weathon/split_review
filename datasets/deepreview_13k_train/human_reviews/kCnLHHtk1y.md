# Building a Special Representation for the Chinese Ancient Buildings in Diffusion models.

- Decision: Reject
- Scores: 3, 5, 1

## Abstract
Benefit from the great generative ability of diffusion models, people can build various images based on their imaginations via some carefully designing prompts. Acctually, the functional blocks, like CLIP, for the alignment between prompts and representation of images plays the key role. Limited by the training data, these models performs worse in some rare areas, like Chinese ancient buildings. The reason comes from the missing of special representation of these building's elements, such as breckets, roofs, bias of different periods. In this paper, we firstly collect more than 400 images of ancient buildings. Several subsets are separated by their generalities.  Secondly, pinyin, the basic tool for learning Chinese,  is firstly introduced into large models as the specific tools to describe the characters of these buildings. Thirdly, we train several fine-tuning models to exhibit the ideal performance of our models compared with existing models. Experiments prove that  our route can resolve the barriers between English-centric models and other cultures.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors proposed to generate Chinese Ancient Buildings with Diffusion models, which is a very interesting  topic. The authors apply pre-trained diffusion models and fine tune it into the specific area where the lora is used. In addition, the authors proposed to use Pinyin as prompts in this specific topic. Furthermore, the authors collect one dataset of Chinese Ancient buildings with about 1200 large-resolution image, which will be benefited for the community. The experimental results by the visual comparison shows the proposed generation methods perform well.

### Strengths
I think there are several strengths attracting me:
(1) The topic is meaningful and interesting. I appreciate the authors' work on this topic, including the trial of applying novel technology (e.g., diffusion and lora) and the experimental results.
(2) The collected dataset seems useful for the related community.
(3) The authors introduced pinyin as prompts into diffusion models, which is promising.

### Weaknesses
(1) I think the big issue of this paper is about the paper-writing, even I suspect some places are not completed. For example, what does the symbols ",,," and "..." mean in the first paragraph?. Also, many writing typos and grammatical mistakes. For example, the sentence “It si similar to the CLIP-diffusion model” seems to be “It is similar to the CLIP-diffusion model”. I suggest that the authors proofread the paper carefully to avoid these.

(2) It is suggested to check the format and completeness of references in the paper. For example, it is incorrect to list reference as Shen et al. (2023), it should be (Shen et al., 2023). In addition, there are some places where references are missing, such as the sentence “Big models in both of CV and NLP area, like ChatGPT and Stable Diffusion” in INTRODUCTION.

(3) The way of citing pictures in the paper is suggested to use Fig. 5, 6 instead of directly an index.  For example, “the visualized results5”, “in different perspectives in 5” and “by SD in 6” in Section 4.3.

(4) In the experimental results, there are only some visualization results. It is suggested that the authors could add more quantitative comparison.

### Questions
Utilizing pinyin sounds reasonable and visualization results shows its effectiveness. However, what about other prompts?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper aims to build representation for Chinese ancient buildings with diffusion models. The authors firstly collect the pictures of the buildings to form the dataset. Then they develop the representation using Pinyin sequence as the prompt input with fine-tuning and LoRA strategies on the diffusion model. Finally, they design experiments to proof the outstanding performance in Chinese ancient building generating area with the learned prompt. This can benefit some specific area like Chinese ancient-style building generation and some down-stream tasks in this community, if any.

### Strengths
The propose of this benchmark can benefit some specific area like Chinese ancient-style building generation and some down-stream tasks in this community, if any.

### Weaknesses
1.	The benchmark is novel and with great effort, while the learned representation and the prompt design are relatively simple. Though the diffusion model is not trained with such specific data, the pre-trained diffusion model still has the ability to generate realistic Chinese ancient buildings (with detailed caption keywords like ‘realistic’). The paper should provide such detailed comparisons.
2.	Lacking qualitative and quantitative comparisons with well-defined metrics like FIDs, CLIPIQA or so to validate the necessity of this benchmark and the special representation development.
3.	Why the Pinyin sequence? Is there a more effective prompt? The authors should provide a more detailed explanation.

### Questions
Why the Pinyin sequence? Is there a more effective prompt? The authors should provide a more detailed explanation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper propose to use diffusion models to generate images of Chinese ancient buildings. The authors adopt pinyin and LoRA to finetune the text encoder of the diffusion model. The experimental results show that the pinyin expression is better than the English expression and the LoRA is better than prompt tuning.

### Strengths
The experimental results show that pinyin and LoRA are effective.

### Weaknesses
1. Lack of novelty: the LoRA is an existing approach.
2. Lack of contribution: the usage of pinyin is trivial.

### Questions
What is the technical novelty of this paper?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
