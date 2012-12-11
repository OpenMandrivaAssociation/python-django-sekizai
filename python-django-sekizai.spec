%define	module	django-sekizai

Summary:	Media framework for Django
Name:		python-%{module}
Version:	0.4.2
Release:	2
Source0:	%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/ojii/django-sekizai/
BuildArch:	noarch
Requires:	python-django-classy-tags >= 0.3.1
BuildRequires:	python-django-classy-tags >= 0.3.1
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx

%description
Sekizai is media (css/js) framework for Django and Django CMS.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sed -i 's/.*egg-info$//' FILE_LIST
pushd docs
make html
popd

%files -f FILE_LIST
%doc LICENSE README.rst docs/_build/html


%changelog
* Mon Dec 19 2011 Lev Givon <lev@mandriva.org> 0.4.2-1
+ Revision: 743818
- imported package python-django-sekizai

