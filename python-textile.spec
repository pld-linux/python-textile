
%define		module	textile

Summary:	Humane Web Text Generator
Summary(pl.UTF-8):   Konwerter czystego tekstu do HTML
Name:		python-%{module}
Version:	2.0.10
Release:	1
License:	GNU
Group:		Development/Languages/Python
# new: http://cheeseshop.python.org/packages/source/t/textile/
Source0:	http://dealmeida.net/code/%{module}-%{version}.tar.gz
# Source0-md5:	19ae07379e5986049b7d9a34ffcbf867
URL:		http://cheeseshop.python.org/pypi/textile
%pyrequires_eq	python-modules
BuildRequires:	python-devel >= 1:2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyTextile is a Python port of Textile, Dean Allen's Humane Web Text
Generator. It's main purpose is to convert plain text to HTML using
popular markup (ie. _something_ means underline, *something* means
emphasis etc.)

%description -l pl.UTF-8
PyTextile jest przepisaną do Pythona wersją programu Textile. Służy on
do konwersji czystego tekstu do formatu HTML, wykorzystując do tego
popularne znaczniki (np. _coś_ oznacza podkreślenie, *coś*
wytłuszczenie itp.)

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

rm $RPM_BUILD_ROOT%{py_sitescriptdir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[co]
