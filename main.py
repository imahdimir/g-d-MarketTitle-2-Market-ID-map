##


from githubdata import GithubData
from mirutil.df_utils import save_df_as_a_nice_xl as sxl
from mirutil.df_utils import read_data_according_to_type as rdata


rp_url = 'https://github.com/imahdimir/d-MarketTitle-2-Market-ID-map'
mkts_rp_url = 'https://github.com/imahdimir/d-Market-ID'

mktitle = 'MarketTitle'
mktid = 'MarketId'


def main() :
  pass

  ##
  rp = GithubData(rp_url)
  rp.clone()
  ##
  cur_module_repo = 'https://github.com/' + rp.usr + '/gov-' + rp.repo_name
  ##
  fpn = rp.data_filepath
  df = rdata(fpn)
  ##
  df = df[[mktitle , mktid]]
  ##
  df = df.sort_values([mktid , mktitle])
  ##
  df = df.drop_duplicates()
  ##
  assert df[mktitle].is_unique
  ##
  mkts_rp = GithubData(mkts_rp_url)
  mkts_rp.clone()
  ##
  udfpn = mkts_rp.data_filepath
  udf = rdata(udfpn)
  ##
  df1 = df[[mktid]].dropna()
  ##
  assert df1[mktid].isin(udf[mktid]).all()
  ##
  sxl(df , fpn)
  ##
  commit_msg = 'checked'
  commit_msg += f' by repo: {cur_module_repo}'

  rp.commit_push(commit_msg)
  ##
  rp.rmdir()
  mkts_rp.rmdir()

  ##


##

##