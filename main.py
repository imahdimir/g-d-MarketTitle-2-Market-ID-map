##

"""

  """

##

from githubdata import GithubData
from mirutil.funcs import norm_fa_str as norm
from mirutil.funcs import save_df_as_a_nice_xl as sxl
from mirutil.funcs import read_data_according_to_type as rdata


map_repo_url = 'https://github.com/imahdimir/d-MarketTitle-2-MarketId'
uniq_fmarkets_repo_url = 'https://github.com/imahdimir/d-uniq-Final-Markets'
cur_module_repo = 'https://github.com/imahdimir/gov-d-MarketTitle-2-MarketId'

mktitle = 'MarketTitle'
mktid = 'MarketId'

def main() :


  pass

  ##
  rp = GithubData(map_repo_url)
  rp.clone()
  ##
  fpn = rp.data_filepath
  ##
  df = rdata(fpn)
  ##
  df = df[[mktitle, mktid]]
  ##
  df = df.sort_values([mktid, mktitle])
  ##
  df = df.drop_duplicates()
  ##
  assert df[mktitle].is_unique
  ##
  ufm_repo = GithubData(uniq_fmarkets_repo_url)
  ufm_repo.clone()
  ##
  udfpn = ufm_repo.data_filepath
  udf = rdata(udfpn)
  ##
  df1 = df[[mktid]].dropna()
  ##
  assert df1[mktid].isin(udf[mktid]).all()
  ##
  sxl(df , fpn)
  ##
  commit_msg = 'sorted'
  commit_msg += f' by repo: {cur_module_repo}'

  rp.commit_push(commit_msg)
  ##
  rp.rmdir()
  ufm_repo.rmdir()

  ##

##