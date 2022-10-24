from django.views.generic import TemplateView, ListView, DetailView, DeleteView, View
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from plc.models import ProductList, PriceList, OutputCsv
from django.contrib.auth.mixins import LoginRequiredMixin
from plc.forms import CreateProductListForm, CreatePriceListForm, CreateOutputCsvForm
import pandas as pd
from django.core import serializers
import math

def ceil(x, s):
    return s * math.ceil(float(x)/s)

TABLE_CLASSES = 'table table-responsive table-bordered table-hover table-sm table-group-divider table-striped table-light'

class return_product_columns(LoginRequiredMixin, View) :
    def get(self, request, pk):
        product_list = ProductList.objects.get(pk=pk)
        data = serializers.serialize('python', [product_list], ensure_ascii=False)
        return JsonResponse(data, safe=False)

class return_price_columns(LoginRequiredMixin, View) :
    def get(self, request, pk):
        price_list = PriceList.objects.get(pk=pk)
        data = serializers.serialize('python', [price_list], ensure_ascii=False)
        return JsonResponse(data, safe=False)

class HomeView(TemplateView):
    template_name = "plc/home.html"

class ProductListView(ListView):
    model = ProductList
    template_name = "plc/product_list.html"
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        product_list = ProductList.objects.all().order_by('-id')
        context['title'] = 'Product List'
        context['product_list'] = product_list
        return context

class ProductListDetailView(DetailView):
    model = ProductList
    template_name = "plc/product_list_detail.html"
    def get(self, request, pk):
        product_list = ProductList.objects.get(id=pk)
        product_list_table = pd.read_csv(product_list.file)
        html_data = product_list_table.to_html(classes=TABLE_CLASSES, index=False)
        context = { 'product_list': product_list, 'title': product_list.title, 'html_data': html_data }
        return render(request, self.template_name, context)

class ProductListCreateView(LoginRequiredMixin, View):
    template_name = 'plc/product_list_form.html'
    success_url = reverse_lazy('plc:product_list')

    def get(self, request, pk=None):
        form = CreateProductListForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateProductListForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        form.save()
        product_list_df = pd.read_csv(form.instance.file)

        # strip whitespace from beginning and end of column_names list items

        # column_names = product_list_df.columns.tolist()
        # column_names_stripped = [column_name.strip(' ') for column_name in column_names]
        # form.instance.column_names = column_names_stripped

        form.instance.column_names = product_list_df.columns.tolist()

        form.save()
        return redirect(self.success_url)

class ProductListUpdateView(LoginRequiredMixin, View):
    template_name = 'plc/product_list_form.html'
    success_url = reverse_lazy('plc:product_list')

    def get(self, request, pk):
        product_list = get_object_or_404(ProductList, id=pk)
        form = CreateProductListForm(instance=product_list)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        product_list = get_object_or_404(ProductList, id=pk)
        form = CreateProductListForm(request.POST, request.FILES or None, instance=product_list)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        product_list.save()
        product_list_df = pd.read_csv(product_list.file)
        product_list.column_names = product_list_df.columns.tolist();
        product_list.save()

        return redirect(self.success_url)

class ProductListDeleteView(LoginRequiredMixin, DeleteView):
    model = ProductList


class PriceListView(ListView):
    model = PriceList
    template_name = "plc/price_list.html"
    def get_context_data(self, **kwargs):
        context = super(PriceListView, self).get_context_data(**kwargs)
        price_list = PriceList.objects.all().order_by('-id')
        context['title'] = 'Price List'
        context['price_list'] = price_list
        return context

class PriceListDetailView(DetailView):
    model = PriceList
    template_name = "plc/price_list_detail.html"
    def get(self, request, pk):
        price_list = PriceList.objects.get(id=pk)
        price_list_table = pd.read_csv(price_list.file)
        html_data = price_list_table.to_html(classes=TABLE_CLASSES, index=False)
        context = { 'price_list': price_list, 'title': price_list.title, 'html_data': html_data }
        return render(request, self.template_name, context)

class PriceListCreateView(LoginRequiredMixin, View):
    template_name = 'plc/price_list_form.html'
    success_url = reverse_lazy('plc:price_list')

    def get(self, request, pk=None):
        form = CreatePriceListForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreatePriceListForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        form.save()
        price_list_df = pd.read_csv(form.instance.file)
        form.instance.column_names = price_list_df.columns.tolist();
        form.save()
        return redirect(self.success_url)

class PriceListUpdateView(LoginRequiredMixin, View):
    template_name = 'plc/price_list_form.html'
    success_url = reverse_lazy('plc:price_list')

    def get(self, request, pk):
        price_list = get_object_or_404(PriceList, id=pk)
        form = CreatePriceListForm(instance=price_list)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        price_list = get_object_or_404(PriceList, id=pk)
        form = CreatePriceListForm(request.POST, request.FILES or None, instance=price_list)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        price_list.save()
        price_list_df = pd.read_csv(price_list.file)
        price_list.column_names = price_list_df.columns.tolist();
        price_list.save()

        return redirect(self.success_url)

class PriceListDeleteView(LoginRequiredMixin, DeleteView):
    model = PriceList

class OutputCsvListView(ListView):
    model = OutputCsv
    template_name = "plc/output_csv_list.html"
    def get_context_data(self, **kwargs):
        context = super(OutputCsvListView, self).get_context_data(**kwargs)
        output_csv_list = OutputCsv.objects.all().order_by('-id')
        context['title'] = 'Output Csv List'
        context['output_csv_list'] = output_csv_list
        return context

class OutputCsvDetailView(DetailView):
    model = OutputCsv
    template_name = "plc/output_csv_detail.html"
    def get(self, request, pk):
        output_csv = OutputCsv.objects.get(id=pk)
        product_list = pd.read_csv(output_csv.product_list.file)
        price_list = pd.read_csv(output_csv.price_list.file)

        PRODUCT_LIST_SEARCH_FIELD = output_csv.product_list_search_field
        PRICE_LIST_SEARCH_FIELD = output_csv.price_list_search_field
        PRODUCT_LIST_REPLACE_FIELD = output_csv.product_list_replace_field
        PRICE_LIST_REPLACE_FIELD = output_csv.price_list_replace_field

        try:
            for _, price_list_row in price_list.iterrows():
                 product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], PRODUCT_LIST_REPLACE_FIELD] = price_list_row[PRICE_LIST_REPLACE_FIELD]
        except:
            raise RuntimeError("Couldn't update product list")

        try:
            output_file = 'output_csvs/output.csv'
            product_list.to_csv(output_file, index=False)
            output_csv.file = output_file
            output_csv.save()
        except:
            raise RuntimeError("Couldn't generate output .csv file")

        output_csv_table = pd.read_csv(output_csv.file)

        output_csv_table.reset_index(drop=True, inplace=True)

        html_data = output_csv_table.to_html(classes=TABLE_CLASSES, index=False)

        context = { 'output_csv': output_csv, 'title': output_csv.title, 'html_data': html_data }
        return render(request, self.template_name, context)


class OutputCsvCreateView(LoginRequiredMixin, View):
    template_name = 'plc/output_csv_form.html'
    success_url = reverse_lazy('plc:output_csv_list')

    def get(self, request, pk=None):
        form = CreateOutputCsvForm()
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        form = CreateOutputCsvForm(request.POST, request.FILES or None)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)
        form.save()

        pk = form.instance.pk
        output_csv = OutputCsv.objects.get(id=pk)
        product_list = pd.read_csv(output_csv.product_list.file)
        price_list = pd.read_csv(output_csv.price_list.file)

        PRODUCT_LIST_SEARCH_FIELD = output_csv.product_list_search_field
        PRICE_LIST_SEARCH_FIELD = output_csv.price_list_search_field
        PRODUCT_LIST_REPLACE_FIELD = output_csv.product_list_replace_field
        PRICE_LIST_REPLACE_FIELD = output_csv.price_list_replace_field

        try:
            for _, price_list_row in price_list.iterrows():
                 product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], PRODUCT_LIST_REPLACE_FIELD] = price_list_row[PRICE_LIST_REPLACE_FIELD]
        except:
            raise RuntimeError("Couldn't update product list")

        try:
            output_file = 'output_csvs/output.csv'
            product_list.to_csv(output_file, index=False)
            output_csv.file = output_file
            output_csv.save()
        except:
            raise RuntimeError("Couldn't generate output .csv file")

        return redirect(self.success_url)

class OutputCsvUpdateView(LoginRequiredMixin, View):
    template_name = 'plc/output_csv_form.html'
    success_url = reverse_lazy('plc:output_csv_list')

    def get(self, request, pk):
        output_csv = get_object_or_404(OutputCsv, id=pk)
        form = CreateOutputCsvForm(instance=output_csv)
        ctx = {'form': form}
        return render(request, self.template_name, ctx)

    def post(self, request, pk=None):
        output_csv = get_object_or_404(OutputCsv, id=pk)
        form = CreateOutputCsvForm(request.POST, request.FILES or None, instance=output_csv)

        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, ctx)

        output_csv.save()
        output_csv = OutputCsv.objects.get(id=pk)
        product_list = pd.read_csv(output_csv.product_list.file)
        price_list = pd.read_csv(output_csv.price_list.file)

        PRODUCT_LIST_SEARCH_FIELD = output_csv.product_list_search_field
        PRICE_LIST_SEARCH_FIELD = output_csv.price_list_search_field
        PRODUCT_LIST_REPLACE_FIELD = output_csv.product_list_replace_field
        PRICE_LIST_REPLACE_FIELD = output_csv.price_list_replace_field

        try:
            for _, price_list_row in price_list.iterrows():
                 product_list.loc[product_list[PRODUCT_LIST_SEARCH_FIELD] == price_list_row[PRICE_LIST_SEARCH_FIELD], PRODUCT_LIST_REPLACE_FIELD] = price_list_row[PRICE_LIST_REPLACE_FIELD]
        except:
            raise RuntimeError("Couldn't update product list")

        try:
            output_file = 'output_csvs/output.csv'
            product_list.to_csv(output_file, index=False)
            output_csv.file = output_file
            output_csv.save()
        except:
            raise RuntimeError("Couldn't generate output .csv file")

        return redirect(self.success_url)

class OutputCsvDeleteView(LoginRequiredMixin, DeleteView):
    model = OutputCsv