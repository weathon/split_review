# On the Coexistence and Ensembling of Watermarks

- Decision: Reject
- Scores: 6, 8, 6, 6

## Abstract
Watermarking, the practice of embedding imperceptible information into media such as images, videos, audio, and text, is essential for intellectual property protection, content provenance and attribution. The growing complexity of digital ecosystems necessitates watermarks for different uses to be embedded in the same media. However, in order to be able to detect and decode all watermarks, they need to coexist well with one another. We perform the first study of coexistence of deep image watermarking methods and, contrary to intuition, we find that various open-source watermarks can coexist with only minor impacts on image quality and decoding robustness. The coexistence of watermarks also opens the avenue for ensembling watermarking methods. We show how ensembling can increase the overall message capacity and enable new trade-offs between capacity, accuracy, robustness and image quality, without needing to retrain the base models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper provides a pioneering investigation into the coexistence and ensembling of watermarking methods, demonstrating that multiple watermarks can coexist in a single image with minimal impact on image quality and decoding accuracy.

### Strengths
1. The paper offers a unique contribution by exploring the coexistence of multiple watermarks within the same image, a topic not previously studied, challenging the assumption that overlapping watermarks would overwrite each other.

2. The paper conducts extensive experiments to validate the coexistence of different watermarks and proposes an effective method for watermark ensembling using strength control and error-correcting codes.

3. The writing of this paper is generally good and easy to understand.

### Weaknesses
1. The authors in this work did not present complete scientific innovation; instead, it focuses more on engineering improvements and exploration, as strength clipping and error correction are relatively mature techniques. I am somewhat concerned about whether the authors have demonstrated sufficient scientific innovation in this work.

2. The authors are encouraged to provide some theoretical justification as to why most watermarking methods can coexist. Additionally, they could offer paradigms, such as which types of watermarking integrations tend to yield better results. For example, it would be helpful to investigate whether watermarks using different hiding techniques, such as frequency and spatial domains, are more easily integrated. This would aid in the design of future watermarking methods.

3. For the initially embedded watermark, the second watermark added actually serves as a form of degradation. Have the authors considered jointly training the encoding and decoding processes of the first and second watermarks? This might lead to better coexistence results.

### Questions
Please refer to the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper studies the coexistence problem of image watermarking methods and explores how to improve the overall information capacity and achieve new trade-offs between quality, capacity, accuracy and robustness by ensembling watermarking methods. Research shows that: 1. although multiple watermarks applied to the same image will lead to a slight decrease in image quality and decoding robustness, different watermarking methods can coexist in the same image and have little impact on their respective decoding accuracy. And 2. by ensembling watermarking methods, the message capacity of the image may increased without retraining the model.

### Strengths
The authors propose and verify the hypothesis that multiple deep learning-based watermarking methods can coexist, providing technical support for the practical need of multi-party watermarking usage. Additionally, through watermark ensembling, the authors demonstrate how capacity can be increased without retraining the base models, offering flexibility for the practical application of watermarking methods. The paper is logically organized and clearly articulated, addressing relevant real-world needs. The experimental design is comprehensive, exploring various combinations of watermarking methods and their impact on image quality, decoding accuracy, and robustness, with persuasive results.

### Weaknesses
1.The coexistence of multiple watermarks was proposed and discussed in the past as an early issue. As the author mentioned, the frequency-based method (one category of watermark coexistence research) and similar studies like [1] . Therefore, when stating the contribution, it would be better to specifically refer to deep learning-based watermark coexistence research.
2. Although the author claims that past frequency-based watermark coexistence research is not applicable to current deep learning-based watermark methods, there is a lack of corresponding discussion and formula derivation. It might be beneficial to include a comparison of relevant methods in the experiments to further enhance persuasiveness.
3. The key figures and table in the paper are very complex. Consider adding more detailed explanations to help readers understand them better.

[1]Xu T, Shao X, Yang Z. Multi-watermarking scheme for copyright protection and content authentication of digital audio[C]//Advances in Multimedia Information Processing-PCM 2009: 10th Pacific Rim Conference on Multimedia, Bangkok, Thailand, December 15-18, 2009 Proceedings 10. Springer Berlin Heidelberg, 2009: 1281-1286.

### Questions
As described in the weakness.

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
This paper analyzes the coexistence of deep-learning-based watermarking schemes and proposes leveraging this coexistence to enable ensemble watermarking models. The authors emphasize the significance of supporting multiple watermarking schemes in practical applications and explore this through extensive experimentation. However, based on the reported results, the benefits of ensembling do not appear clearly advantageous when considering the capacity-robustness-quality trade-off.

### Strengths
1. This paper investigates the coexistence of deep-learning-based watermarking schemes. The coexistence problem is an important aspect for practical application.
2. The study provides comprehensive experimental analyses on the coexistence and ensembling of watermarks. These results are valuable for further studies.

### Weaknesses
1. The conditions for robustness testing are not fully explained. Section 2 contains ambiguous phrases, such as "augmentations used for training RivaGAN." Clear details on the types of attacks used, each attack's strength, and the methodology for calculating the robustness values would improve clarity.
2. The effectiveness of ensembling under varying attack strengths needs further verification. Given that robustness is achieved through ECC, it would be beneficial to assess whether the proposed method can withstand strong attacks.
4. Despite the inclusion of ECC, the observed robustness values appear insufficient for practical applications.
3. Figure 5 does not demonstrate an improvement in the overall capacity-robustness-quality trade-off with ensembling. For example, in sub figure B, ensembling reduces robustness compared to TrustMark. Although a slight improvement in quality is noted, it does not suggest that ensembling offers a better trade-off.

### Questions
Please refer to the Weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This manuscript starts from the consideration of two possible scenarios that need to add several watermarks from different sources into the same carrier: the addition of  super watermark to inform the user which watermark detector to use for this image, and different users would use different watermarks for their content provenance goals. Based on these demands, authors point out the need and importance for different watermarks to simultaneously exist in the same carrier. Thus, authors conduct ample experiments on various watermarking methods to add the new watermark information into the image containing another watermark message to check whether or not watermark messages from various sources can co-exist in the same image.  The experimental result shows that, different from the expectation of many peoples that watermarks may overwrite each other, in most situations, after adding the second watermark, the first watermark message can still be decoded with a high accuracy even if confinements are made to avoid the degradation of visual quality or robustness caused by the existence of two watermarks. And authors claim that to their knowledge, watermark coexistence has not been studied before. With this finding, the manuscript proposes to utilize the watermark coexistence to modify the performance of existing methods without needing any retraining, and sometimes this may bring the enhancement of some factors in capacity, accuracy, robustness, and visual quality.

### Strengths
1. As the claim of authors, this manuscript firstly try to explore the watermark coexistence, which is a valuable attempt and interesting perspective in the field of watermarking, and this work may inspire more researchers to involve in the filling of existing research blanks of watermarking technology.
2. It is good for authors of this manuscript to find out two persuasive scenarios to demonstrate the demand to contain multiple watermarks in a same coverage, which can contribute to the application meaning of the research in this manuscript, and demonstrate authors' good understanding about the application situation of watermarking technology in the real scenario.
3. To verify that different watermarks can co-exist simultaneously, authors conducted an ample amount of experiments to provide sufficient experimental evidence. The considerable volume of work completed by authors is an advantage of this work. 
4. After finding the watermark coexistence, authors propose two straightforward methods to add multiple watermarks into the image: serial method and parallel method. Even if they are easy methods without the complex design, they can actually be implemented by users with the need to embed several different watermarks, so as to directly meet the related demand, obtaining certain application value.
5. The organization of this paper is clear and readable. Authors starts from the demand in the real scenario, then use experiments to verify the existence of watermark coexistence, and the analysis about the experimental can also help to illustrate the research of this manuscript. After that, methods to utilize the watermark coexistence are proposed, with experiments conducted to test the performance. The thinking of authors when writing this manuscript can be easily captured, which is beneficial for readers to better understand this work.

### Weaknesses
1. In the Introduction of this manuscript, authors claim that the same principles found in this manuscript likely apply also to video, audio, and to some extent, text watermarking. However, this paper just focus on the image watermarking methods, which fails to give persuasive evidence to illustrate this point. So authors can modify the expression of this manuscript to just focus on image watermarking, or consider to add some experiments using audio or text watermarking methods to prove their opinion.

2. As written by authors, this manuscript can successfully find out the watermark coexistence phenomenon, but fails to figure out the root causes of this phenomenon. Authors are encouraged to give some theoretical analysis to get closer to the real factor causing the watermark coexistence. This is also beneficial for the improvement of academic meaning of this manuscript.

3. This manuscript's findings and contributions are significantly based on the experiments or the reutilization about existing methods. Even if this still has its meaning, the further exhibition about the novelty of this manuscript  is inevitably affected. It would be better for authors to go further with their acquired findings shown in this manuscript and better strengthen the novelty of their work.

4. In the experiment, authors find that in some cases, a strong base method with ECC can perform better than ensembling. This will do harm to the convenient utilization of ordinary users about adding different watermarks, because it will not be so easy for ordinary users to decide whether or not the combination of watermarking methods they want to use can definitely achieve ideal performance they desire compared to returning to a strong base method with ECC.  

5. The spelling mistake should  be eliminated in the next version of this manuscript. For example, in about line 63, the shown "neeeding" should be corrected to "needing".

### Questions
1. There lacks the evidence to prove the watermark coexistence can still be seen in other categories of carriers different from images. Authors can modify the expression of this manuscript to just focus on image watermarking, or consider to add some experiments using audio or text watermarking methods to prove their opinion.

2. Authors are encouraged to give more theoretical analysis to try to find out the root reason causing the watermark coexistence, which is also beneficial for the improvement of academic value of this manuscript.

3. Based on their acquired findings shown in this manuscript, it would be better for authors to go further and show more special contributions less relying on previous achievements, so as to  strengthen the novelty of their work.

4. Authors should manage to find a method to better instruct ordinary users to correctly find watermarking methods that can really achieve desired performance with the utilization of watermark coexistence, compared to just use one strong base method with ECC. 

5. Typos should  be fixed after the revision of this manuscript. For example, in about line 63, the shown "neeeding" should be changed to "needing".

### Soundness
3

### Presentation
3

### Contribution
3
