import torch
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image

def fruitPredict(file_path):

    SAVE_PATH = r"C:\Users\kdp\KDT_06\KDT\EX_PY06\KDT\Project10\models\project" # 웹상에서는 절대경로만
    SAVE_MODEL = SAVE_PATH +'\loss_0.083_score0.976.pth'

    target = ['Apple', 'Banana', 'Orange', 'Strawberry']

    Model = torch.load(SAVE_MODEL, weights_only= False, map_location=torch.device('cpu'))
    # GPU에서 생성한 모델 => 모델 로드 시 map_location=torch.device('cpu')

    transform = transforms.Compose([transforms.Resize([256]), transforms.CenterCrop(224),transforms.ToTensor(),
                           transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    
    file = file_path

    image = Image.open(file).convert('RGB')
    pil_image = transform(image).unsqueeze(0)

    # 모델 테스트
    Model.eval()
    result = Model(pil_image)

    idx = result.argmax().item()

    return target[idx]


def fruitPredict2(file):

    SAVE_PATH = r"C:\Users\kdp\KDT_06\KDT\EX_PY06\KDT\Project10\models\project" # 웹상에서는 절대경로만
    SAVE_MODEL = SAVE_PATH +'\loss_0.083_score0.976.pth'

    target = ['Apple', 'Banana', 'Orange', 'Strawberry']

    Model = torch.load(SAVE_MODEL, weights_only= False, map_location=torch.device('cpu'))
    # GPU에서 생성한 모델 => 모델 로드 시 map_location=torch.device('cpu')

    transform = transforms.Compose([transforms.Resize([256]), transforms.CenterCrop(224),transforms.ToTensor(),
                           transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

    # transform = v2.Compose([transforms.Resize([256]), v2.CenterCrop(224),v2.ToTensor(),
    #                        v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])

    file = r'C:\Users\kdp\KDT_06\KDT\EX_PY06\KDT\Project10\images' + '\\' + file

    image = Image.open(file).convert('RGB')
    pil_image = transform(image).unsqueeze(0)

    # pil_image = transform(file)

    # 모델 테스트
    Model.eval()
    result = Model(pil_image)

    idx = result.argmax().item()

    return target[idx]

result = fruitPredict2('banana01.jpg')
print(result)