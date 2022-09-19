from .uav import UAVDataset
from .dtb import DTBDataset
from .uav10fps import UAV10Dataset
from .uav20l import UAV20Dataset
class DatasetFactory(object):
    @staticmethod
    def create_dataset(**kwargs):
        """
        Args:
            name: dataset name 'OTB2015', 'LaSOT', 'UAV123', 'NFS240', 'NFS30',
                'VOT2018', 'VOT2016', 'VOT2018-LT'
            dataset_root: dataset root
            load_img: wether to load image
        Return:
            dataset
        """
        assert 'name' in kwargs, "should provide dataset name"
        name = kwargs['name']
        if 'DTB' in name:
            dataset = DTBDataset(**kwargs)
        elif 'UAV10' in name:
            dataset = UAV10Dataset(**kwargs)
        elif 'UAV20' in name:
            dataset = UAV20Dataset(**kwargs)
        elif 'UAV123' in name:
            dataset = UAVDataset(**kwargs)

        else:
            raise Exception("unknow dataset {}".format(kwargs['name']))
        return dataset

